# Fiscorex Email Design System

Design system untuk email outbound Fiscorex (dibuat dari referensi email "See If You Qualify").

| File | Fungsi |
|---|---|
| `tokens.json` | Sumber kebenaran: warna, tipografi, spacing, layout |
| `tokens.css` | Variabel CSS untuk preview/dokumentasi saja |
| `email-base.html` | Template email siap pakai (table-based, inline style) |
| `preview.html` | Halaman visual: swatch, tipografi, komponen |
| `assets/` | Taruh `logo.png` (logo Fiscorex, ±440px lebar @2x) di sini |

## 1. Prinsip
- **Tenang & tepercaya** – tone compliance/administratif, bukan hard-sell.
- **Satu pesan, satu CTA** – satu tombol per email.
- **Teks seperti surat** – email terasa personal: salam nama, paragraf pendek, tanda tangan manusia.
- **Disclaimer selalu ada** – Fiscorex bukan penasihat pajak/hukum; jangan menjanjikan hasil spesifik.

## 2. Warna
| Token | Hex | Pemakaian |
|---|---|---|
| brand-green | `#0B4A33` | Logo, link brand |
| navy | `#14213A` | Tombol CTA, footer |
| surface | `#F8F8F4` | Background body & header |
| canvas | `#E9EDF4` | Background luar email |
| border | `#DDDDD6` | Garis bawah header |
| text | `#111111` | Teks utama |
| footer-text | `#8591A8` | Teks footer di atas navy |
| footer-muted | `#66738C` | Baris tersier footer |

Kontras: teks `#111` di `#F8F8F4` ≈ 17:1; label putih di navy ≈ 16:1. Teks footer `#8591A8` di navy ≈ 5:1 (AA, ukuran 12px—jangan dipakai lebih redup).

## 3. Tipografi
- Font: `Verdana, 'DejaVu Sans', Geneva, Tahoma, sans-serif` (web-safe, tanpa web font).
- Body 16px / 1.55 · H1 24 · H2 20 · Small 12 / 1.6.
- Paragraf: `margin: 0 0 16px`. Sebelum CTA: 32px.

## 4. Layout
- Lebar 600px, rata tengah; mobile (<620px) jadi 100% dengan padding 20px.
- Body padding 40px; header padding 24×40; footer padding 32×40.
- Struktur wajib: **Header (logo) → Body → CTA → Sign-off → Footer navy**.

## 5. Komponen
**Header** – logo terpusat (lebar 220px), background surface, border bawah 1px `#DDDDD6`.

**Body copy** – sapaan `Hi {{contact.first_name}},` lalu 2–4 paragraf pendek (1–3 kalimat).

**Primary button** – navy `#14213A`, label putih 16px/500, padding 14×28, radius 8, di tengah. Label berupa aksi ("See If You Qualify"). Gunakan pola `<td bgcolor>` + `<a>` (bulletproof, aman di Outlook).

**Sign-off** – `John Krowiak` lalu `The Fiscorex Team`.

**Footer** – background navy, teks 12px rata tengah: (1) disclaimer, (2) copyright · kota · `+1 888-493-2881` · email (link underline), (3) unsubscribe.

## 6. Merge tag (GoHighLevel)
`{{contact.first_name}}`, `John Krowiak`, `+1 888-493-2881`, `{{unsubscribe_link}}`, `{{trigger_link.link}}` (ganti dengan trigger link sebenarnya).

## 7. Aturan penulisan
- Subjek ≤ 50 karakter, tanpa huruf kapital semua/tanda seru.
- Hindari klaim absolut ("pasti hemat", "dijamin"); gunakan "banyak perusahaan", "kebanyakan perusahaan dapat memenuhi syarat".
- Sebut disclaimer non-advisor di body bila membahas pajak/benefit.
- CTA bersifat low-commitment ("See if you qualify", "no-obligation call").

## 8. Aturan teknis email
- Layout `<table role="presentation">`, semua style **inline**; `<style>` hanya untuk media query.
- Tanpa web font, tanpa JS, tanpa background-image penting.
- Semua gambar punya `alt`; logo PNG (bukan SVG) untuk kompatibilitas Outlook.
- `color-scheme: light only` agar tidak dibalik dark mode secara acak.
- Sertakan preheader tersembunyi (≤ 90 karakter).
- Tes di Gmail, Outlook (desktop), Apple Mail, dan mobile sebelum kirim.

## 9. Catatan
- Hex warna diperkirakan dari screenshot; sesuaikan bila ada brand guideline resmi.

- Logo dimuat dari URL absolut (PNG, CDN GoHighLevel): `https://assets.cdn.filesafe.space/2N22VRJfVoGJEc4GpJzv/media/6a96d043c7069f4fc798d774.png`. Gunakan PNG, bukan WebP, agar tampil di Outlook desktop.