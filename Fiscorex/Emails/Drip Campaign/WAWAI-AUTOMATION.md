# Fiscorex Drip — Wawai Mail automation

**Status: RUNNING since 2026-10-27 ("go"). Progress is in `drip-state.json`; a daily check (15:17 UTC) runs whatever steps are due.**

- Wawai sub-account: `f723af01-f6f2-4edf-b3a6-9f1b0161273b` (Fiscorex), data source `native`, from name `John Krowiak` (default set in Wawai; sends from fiscorex@mail.willsupportyou.com)
- Audience: groups `Drip-01` to `Drip-12` (see below)
- HTML: `python3 to_wawai.py <email-file>` (swaps GHL images/merge tags for Wawai ones, prints subject to stderr)
- Every email gets a small John Krowiak photo beside the signature (added by the converter).

## Subject lines

- EMAIL-01 send (Day 1): `Could you save up to $1,186 per eligible employee annually?`
- EMAIL-01 resend (Day 3): `Did you know you can save up to $1,186 per eligible employee annually?`
- EMAIL-02 to EMAIL-10 (send and resend): the subject in each file's header comment.

Wawai contacts have no first name, so the name is left out of the Day 1 subject (and the body greeting is "Hi there,").

## Contacts and failed emails

- Source: the Fiscorex SIMERP scored CSV (599 rows, 591 with an email). Not committed (personal data). **Imported 2026-10-27** into 12 groups (`Drip-01` to `Drip-12`, highest intent score first; private mapping with Email 2 in `drip-contacts.csv`, not committed), 50 contacts each (last has 41); group N starts N-1 days after "go".
- Failure rule: no delivered record 24 hours after a contact's first EMAIL-01 send. Failed contacts are **reported only**: nothing more is sent to them, and no Email 2 fallback unless the user asks. No test send was run.
- Every failure is logged (Email 2 column kept for reference) to `invalid-emails.csv` (not committed) for pasting into the "Invalid Email" tab of the Google Sheet.

## Schedule (Day 1 = the day you say "go")

| Day | Step | Audience |
|---|---|---|
| 1 | Send EMAIL-01 | segment |
| 3 | Resend EMAIL-01 | non-clickers of Day 1 |
| 6 | Send EMAIL-02 | segment |
| 9 | Resend EMAIL-02 | non-clickers of Day 6 |
| 13 | Send EMAIL-03 | segment |
| 16 | Resend EMAIL-03 | non-clickers of Day 13 |
| 20 | Send EMAIL-04 | segment |
| 23 | Resend EMAIL-04 | non-clickers of Day 20 |
| 28 | Send EMAIL-05 | segment |
| 31 | Resend EMAIL-05 | non-clickers of Day 28 |
| 37 | Send EMAIL-06 | segment |
| 40 | Resend EMAIL-06 | non-clickers of Day 37 |
| 47 | Send EMAIL-07 | segment |
| 50 | Resend EMAIL-07 | non-clickers of Day 47 |
| 58 | Send EMAIL-08 | segment |
| 61 | Resend EMAIL-08 | non-clickers of Day 58 |
| 71 | Send EMAIL-09 | segment |
| 74 | Resend EMAIL-09 | non-clickers of Day 71 |
| 87 | Send EMAIL-10 | segment |
| 90 | Resend EMAIL-10 | non-clickers of Day 87 |

## How it runs

Wawai has no built-in automation or "if not clicked" branch, and a scheduled send is charged when it is scheduled. So on "go", Claude sets one session check-in per row above, and each check-in does:

- **Send:** `preview_campaign(segment, subject)` → `confirm_send(preview_hash, html, subject)`. Record the campaign id in the log below.
- **Resend:** `get_campaign_recipients(<send's campaign id>)` → everyone without a click is tagged into group `Drip-NN-NoClick` with `import_contacts` → `preview_campaign("Drip-NN-NoClick", subject)` → `confirm_send`. Skipped if everyone clicked.

Limitation: Wawai records clicks per email, not per link, so a click on any link (logo, phone, email, Calendly) counts as "clicked the button".

## Send log

| Day | Step | Date | Campaign id | Recipients |
|---|---|---|---|---|
