# Fiscorex Drip Campaign

Semua email memakai [email-base.html](../../design systems/email-base.html) (header, footer, tombol CTA, token yang sama). Hanya konten body, subject, dan preheader yang berubah.

## Urutan (usulan)
| # | Timing | Tema | Subject | CTA | File |
|---|---|---|---|---|---|
| 01 | Day 0 (alternate Day 3) | The FICA Advantage Program | {{contact.first_name}}, could you save up to $1,186 per eligible employee annually? | Schedule Now | `email-01-fica-advantage-program.html` |
| 02 | Day 6 (alternate Day 9) | A Simple Way to Lower Payroll Tax Overhead | A simple way to lower payroll tax overhead | Schedule Now | `email-02-lower-payroll-tax-overhead.html` |
| 03 | Day 12 (alternate Day 15) | Where the FICA Savings Actually Come From | Where the FICA savings actually come from | Schedule Now | `email-03-where-fica-savings-come-from.html` |
| 04 | Day 19 (alternate Day 22) | What Your Employees Get, at No Added Cost | What your employees get, at no added cost | Schedule Now | `email-04-employee-benefits.html` |
| 05 | Day 26 (alternate Day 29) | Does This Replace Your Current Health Plan? | Does this replace your current health plan? | Schedule Now | `email-05-replace-current-health-plan.html` |
| 06 | Day 33 (alternate Day 36) | Built to Align with IRS Section 125 and 105 Rules | Built to align with IRS Section 125 guidelines | Schedule Now | `email-06-section-125-105-compliance.html` |
| 07 | Day 41 (alternate Day 44) | What the Up to $1,186 Estimate Is Based On | What that up to $1,186 per-employee estimate is based on | Schedule Now | `email-07-savings-estimate.html` |
| 08 | Day 50 (alternate Day 53) | What Setup Actually Looks Like | What setup actually looks like | Schedule Now | `email-08-what-setup-looks-like.html` |
| 09 | Day 60 (alternate Day 63) | A Benefit Employees Actually Use | A benefit employees actually use | Schedule Now | `email-09-benefit-employees-use.html` |
| 10 | Day 72 (alternate Day 75) | The Questions Every CFO Asks First | The questions every CFO asks us first | Schedule Now | `email-10-cfo-questions.html` |
| 11 | Day 87 (alternate/final Day 90) | Graceful, Low-Pressure Close | Worth 30 minutes, whenever the timing's right | Schedule Now | `email-11-soft-close.html` |

## Aturan drip
- Satu CTA per email; nada tenang, tanpa klaim absolut, disclaimer non-advisor tetap di footer.
- Email 1–3 CTA sama (cek kelayakan); email 4 beralih ke panggilan.
- Hentikan sequence bila kontak: klik/menyelesaikan kualifikasi, booking, balas, atau unsubscribe.
- Kirim di jam kerja lokal penerima (Selasa–Kamis lebih baik).
- Setiap file diberi komentar di atas HTML: subject, preheader, tujuan, dan kondisi exit.

## Merge tag
`{{contact.first_name}}`, `John Krowiak`, `+1 888-493-2881`, `{{unsubscribe_link}}`
