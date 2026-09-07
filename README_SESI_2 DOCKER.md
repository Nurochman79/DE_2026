# Sesi 2 — Paket Bahan Ajar

**Fullstack Bangalore · Data Engineer Bootcamp Advanced**
Pertemuan 2 · 2 jam · Phase 0: Mindset & Environment

## Isi folder

| Yang mana | Untuk siapa | Isinya |
| --- | --- | --- |
| `Sesi_02_Docker_Environment_yang_Bisa_Diulang.pptx` | dipresentasikan | 30 slide di atas template FSB, tanpa speaker notes |
| `Catatan_Instruktur_Sesi_2.md` | instruktur saja | bahan bicara per slide, termasuk kunci jawaban dua Cek Paham |
| `sesi2-docker.zip` | **dibagikan ke peserta** | repo praktik, siap dibuka |
| `sesi2-docker/` | instruktur | isi zip di atas, versi yang sudah dijalankan |
| `_tools_deck/` | instruktur | generator deck dan skrip pengecek tata letak |

**Yang dibagikan ke peserta cuma `sesi2-docker.zip`.** File catatan instruktur
berisi kunci jawaban, jangan ikut dikirim.

---

## Sebelum mengajar

Nyalakan Docker Desktop dulu, lalu:

```bash
cd sesi2-docker
docker compose up -d --build
docker compose exec pipeline python 01_buat_data.py
docker compose exec pipeline python 02_bronze.py
docker compose exec pipeline python 03_silver.py
docker compose exec pipeline python 04_gold.py
docker compose exec pipeline python 05_lihat_hasil.py
docker compose exec pipeline python -m pytest test_pipeline.py -v
```

Simpan output terminalnya. Itu patokan angka di kelas.

Angka yang harus muncul (seed 42, sama persis dengan Sesi 1):

```
bronze          :  2053 baris masuk
kiriman ganda   :    53 baris
order unik      :  2000 baris
ditolak         :    90 baris
silver          :  1910 baris
lolos           : 95.5%

TOTAL PENJUALAN  Rp 630.614.700
TOTAL LABA       Rp 159.089.700   margin 25,2%
```

7 passed di pytest.

Kalau angkanya beda, hampir pasti `01_buat_data.py` dijalankan dua kali.
Bereskan dengan `docker compose down -v` lalu mulai lagi dari awal.

---

## Alur sesi

| Menit | Slide | Isi |
| --- | --- | --- |
| 0–10 | 1–3 | Pembuka, daftar materi, kasus "jalan di laptop saya" |
| 10–30 | 4–5 | Image, container, registry, daur hidup |
| 30–50 | 6–9 | Dockerfile, layer caching, volume, cek paham 1 |
| 50–70 | 10–14 | Jaringan, Compose, live debug, cek paham 2, bedah Sesi 1 vs 2 |
| 70–75 | 15–16 | Brief praktik dan pengecekan environment |
| 75–105 | 17–21 | Praktik: nyalakan, jalankan, pgAdmin, dua bukti, sabotase |
| 105–120 | 22–30 | Bedah hasil, error umum, debrief, topologi, tugas, penutup |

Tiga checkpoint yang diminta kurikulum:

1. **Environment ready** — slide 16, semua sudah lihat `docker --version`.
2. **Core build works** — slide 18, angka peserta cocok dengan angka kelas.
3. **Evaluation ready** — slide 20, dua bukti (isolasi jaringan dan volume)
   sudah dijalankan sendiri.

---

## Praktik: satu repo, sembilan file

| File | Yang dikerjakan | Baris |
| --- | --- | --- |
| `Dockerfile` | Resep image pipeline | 40 |
| `docker-compose.yml` | 3 layanan, 2 jaringan, 2 volume | 118 |
| `app/db.py` | Koneksi database, dengan tunggu-dan-ulang | 67 |
| `app/01_buat_data.py` | Bikin 3 file CSV dummy | 140 |
| `app/02_bronze.py` | CSV masuk Postgres apa adanya | 68 |
| `app/03_silver.py` | Bersihkan, yang salah masuk `data_ditolak` | 139 |
| `app/04_gold.py` | Ringkas jadi tiga tabel angka | 84 |
| `app/05_lihat_hasil.py` | Tampilkan hasilnya | 52 |
| `app/test_pipeline.py` | Tujuh pemeriksaan | 65 |

Logikanya sama persis dengan Sesi 1. Yang berubah cuma tempat datanya dan
lima perbedaan dialek SQL antara SQLite dan PostgreSQL — daftarnya ada di
`sesi2-docker/README.md`.

---

## Angka yang dipakai di slide

Semuanya hasil ukur sungguhan di repo ini, bukan perkiraan:

| Yang dipakai | Nilai | Di slide |
| --- | --- | --- |
| Build tanpa perubahan | 3 detik | 7 |
| Build setelah ubah satu baris kode | 1 detik | 7 |
| Build setelah ubah `requirements.txt` | 11 detik | 7 |
| Bukti isolasi jaringan | `socket.gaierror` | 10, 20 |
| Bukti volume | `Rp 630.614.700` setelah `down` + `up` | 8, 20 |
| Error pgAdmin di Live Debug | email `.local` ditolak | 12 |

Error pgAdmin di slide 12 memang terjadi waktu materi ini disiapkan. Cara
memperagakannya: ubah `PGADMIN_EMAIL` di `.env` jadi `admin@toko.local`, lalu
`docker compose up -d pgadmin`. Containernya akan mati dengan `Exited (1)`.

---

## Tiga hal yang paling penting disampaikan

1. **Angka Sesi 1 dan Sesi 2 harus sama persis.** Kalau bergeser satu baris
   saja, berarti ada yang tidak ikut terbawa waktu pindah environment. Itu
   inti dari kata *reproducible*.
2. **Volume dan container umurnya beda.** `down` menghapus container, `down -v`
   ikut menghapus volume. Ucapkan pelan, ulangi.
3. **Error `gaierror` di slide 10 dan 20 itu hasil yang benar.** Peserta perlu
   menjalankannya sendiri, bukan cuma percaya slide.

---

## Mengecek deck setelah diubah

```powershell
cd _tools_deck
python s2_build.py
.\audit.ps1 -Deck "..\Sesi_02_Docker_Environment_yang_Bisa_Diulang.pptx" -Out shapes.csv
python analyze.py
```

Tiga pemeriksaan harus kosong: isi yang keluar kartu, teks tertimpa kotak, dan
teks bertabrakan dengan teks lain.

**Hati-hati:** `s2_build.py` menulis ulang file `.pptx` dari nol. Editan manual
di PowerPoint akan hilang. Kalau sudah terlanjur mengedit, jalankan
`bandingkan.py` dulu untuk melihat apa saja yang berbeda.

---

## Sambungan ke sesi berikutnya

Sesi 3 (*Your Big Data Lab*) menambah Kafka, MinIO, dan Jupyter ke file
`docker-compose.yml` yang sama. Karena itu:

- Minta peserta **jangan** menjalankan `docker compose down -v` setelah kelas.
- Minta yang laptopnya RAM 8 GB memberi tahu dari sekarang, supaya bisa
  disiapkan susunan yang lebih hemat.
