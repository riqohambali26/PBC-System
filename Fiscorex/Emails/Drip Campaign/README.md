# Fiscorex Drip Campaign

Semua email memakai [email-base.html](../../design systems/email-base.html) (header, footer, tombol CTA, token yang sama). Hanya konten body, subject, dan preheader yang berubah.

## Urutan (usulan)
| # | Hari | Tema | Subject | CTA | Status |
|---|---|---|---|---|---|
| 01 | 0 | Perkenalan: manfaat + ajakan cek kelayakan | A way to cut payroll tax overhead and add health benefits | See If You Qualify | **Selesai** → `email-01-introduction.html` |
| 02 | 2–3 | Versi singkat: potensi pengurangan FICA match, tanpa ganti asuransi | The short version | See If You Qualify | **Selesai** → `email-02-short-version.html` |
| 03 | 5–6 | Benefit karyawan: telemedicine, primary care, mental health, nurse coaching | What your employees actually get | See If You Qualify | **Selesai** → `email-03-employee-benefits.html` |
| 04 | 9–10 | Pertanyaan umum: apakah menggantikan asuransi? (tidak, melengkapi) | Does this replace our current insurance? | See If You Qualify | **Selesai** → `email-04-insurance-question.html` |
| 05 | 14 | Compliance (sudut pandang CFO): IRS Section 125 & 105, dokumentasi | Compliance: what a CFO will want to know | See If You Qualify | **Selesai** → `email-05-compliance.html` |
| 06 | 18–19 | Estimasi penghematan per karyawan: rata-rata, bukan jaminan | About that savings estimate | See If You Qualify | **Selesai** → `email-06-savings-estimate.html` |
| 07 | 22–23 | Beban admin HR/payroll: integrasi ADP, Paychex, Gusto | Will this create more work for HR? | See If You Qualify | **Selesai** → `email-07-admin-burden.html` |
| 08 | 26–27 | Pengalaman karyawan: app sederhana, $0-copay, recruiting & retention | Benefits people actually use | See If You Qualify | **Selesai** → `email-08-employee-experience.html` |
| 09 | 30–31 | Rangkuman pertanyaan umum: compliance, take-home pay, beban admin | The three questions we hear most | See If You Qualify | **Selesai** → `email-09-common-questions.html` |
| 10 | 35–37 | Penutup lembut (soft close), tanpa tekanan | No pressure either way | See If You Qualify | **Selesai** → `email-10-soft-close.html` |

## Aturan drip
- Satu CTA per email; nada tenang, tanpa klaim absolut, disclaimer non-advisor tetap di footer.
- Email 1–3 CTA sama (cek kelayakan); email 4 beralih ke panggilan.
- Hentikan sequence bila kontak: klik/menyelesaikan kualifikasi, booking, balas, atau unsubscribe.
- Kirim di jam kerja lokal penerima (Selasa–Kamis lebih baik).
- Setiap file diberi komentar di atas HTML: subject, preheader, tujuan, dan kondisi exit.

## Merge tag
`{{contact.first_name}}`, `John Krowiak`, `+1 888-493-2881`, `{{trigger_link.link}}`, `{{unsubscribe_link}}`
