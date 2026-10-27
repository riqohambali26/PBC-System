"""Convert a drip email (GHL-flavoured HTML) into HTML Wawai Mail accepts.

Usage: python3 to_wawai.py email-01-introduction.html > out.html
Prints the subject to stderr.
"""
import re
import sys

# Wawai only allows images uploaded through its own tool (tenant f723af01-..., Fiscorex).
ASSET = "https://wawai-email-sender-campaign-assets-314567759774.s3.us-east-1.amazonaws.com/f723af01-f6f2-4edf-b3a6-9f1b0161273b/"
IMAGES = {
    "https://assets.cdn.filesafe.space/2N22VRJfVoGJEc4GpJzv/media/6a96d043c7069f4fc798d774.png": ASSET + "4d91bc5a-2044-4049-ba51-f88c81a64a6c.png",  # logo
    "https://assets.cdn.filesafe.space/2N22VRJfVoGJEc4GpJzv/media/6a96d0439b2eaead5c1929e8.jpeg": ASSET + "2bcb62f7-cbf8-4e32-b98c-a710e57ee90a.jpg",  # John Krowiak
}
# Subjects that replace the one in the file's header comment: file -> (send, resend).
SUBJECTS = {
    "email-01-introduction.html": (
        "Could you save up to $1,186 per eligible employee annually?",
        "Did you know you can save up to $1,186 per eligible employee annually?",
    ),
}
JOHN = "https://assets.cdn.filesafe.space/2N22VRJfVoGJEc4GpJzv/media/6a96d0439b2eaead5c1929e8.jpeg"
UNSUB = '<p style="margin:0;color:#66738C;">Want to change'


def convert(src, name=""):
    subject = re.search(r"Subject:\s*(.+)", src).group(1).strip()
    subject = SUBJECTS.get(name, (subject,))[0]
    html = src[src.index("<!DOCTYPE"):]  # drop the notes comment above the doctype
    for old, new in IMAGES.items():
        html = html.replace(old, new)
    # Small headshot beside the signature (the lines after the SIGN-OFF marker, ending at the phone number).
    html, n = re.subn(
        r'(<!-- SIGN-OFF -->\n)(.*?\(888\) 493-2881</a></p>\n)',
        lambda m: m.group(1)
        + '<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>\n'
        + '<td valign="top" style="padding-right:16px;"><img src="' + IMAGES[JOHN] + '" alt="John Krowiak" width="90" style="display:block;width:90px;height:auto;border-radius:8px;"></td>\n'
        + '<td valign="top">\n' + m.group(2) + '</td></tr></table>\n',
        html, count=1, flags=re.S)
    assert n == 1, "signature block not found"
    # Wawai contacts have no first name field.
    html = html.replace("Hi {{contact.first_name}},", "Hi there,")
    html = html.replace("{{unsubscribe_link}}", "{{unsubscribe_url}}")
    html = html.replace(UNSUB, '<p style="margin:0 0 16px;color:#8591A8;">{{sender_footer}}</p>\n        ' + UNSUB)
    for leftover in ("filesafe.space", "{{contact.", "{{unsubscribe_link}}"):
        assert leftover not in html, leftover
    assert html.count("{{sender_footer}}") == 1 and "{{unsubscribe_url}}" in html
    return subject, html


if __name__ == "__main__":
    subject, html = convert(open(sys.argv[1], encoding="utf-8").read(), sys.argv[1])
    print(subject, *SUBJECTS.get(sys.argv[1], ())[1:], sep="\n  resend: ", file=sys.stderr)
    sys.stdout.write(html)
