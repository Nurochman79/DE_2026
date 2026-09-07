# SQLite Warehouse — Engineering Delivery Pack

## Context
Anda bergabung sebagai engineer yang menerima data transaksi hasil proses upstream. Tim Finance membutuhkan SQLite warehouse lokal sebagai sumber angka operasional. Data sudah valid secara format, tetapi integritas relasinya belum dijamin.

Anda menerima repository, kontrak data, acceptance criteria, dan quality gates. Sebagai owner ticket, Anda bertanggung jawab menghasilkan delivery yang dapat direproduksi dan direview engineer lain.

## Work Order
Ambil ticket di `PROJECT_BRIEF.md`. Implementasi utama berada di:
- `schema.sql`
- `queries.sql`
- `src/warehouse.py`

Jangan mengubah input di `data/processed/`. Notebook hanya untuk inspeksi dan review evidence, bukan tempat menyimpan implementasi alternatif.

## Definition of Done
Delivery dinyatakan siap review jika:
- pipeline dapat dibangun ulang dari kondisi bersih;
- constraint database menolak referensi yang tidak valid;
- row gagal tercatat dengan alasan yang dapat diaudit;
- metric bisnis sesuai acceptance criteria;
- notebook dan CLI menghasilkan evidence yang konsisten;
- `python validate_delivery.py` berakhir dengan `READY FOR REVIEW`.

## Engineering Workflow
1. **Triage repository** — jalankan `python preflight.py`, baca ticket dan data contract.
2. **Design** — catat keputusan grain, PK/FK, nullability, dan checks di `workpapers/SCHEMA_CANVAS.md`.
3. **Implement** — kerjakan schema, loader, reject handling, dan query.
4. **Test incrementally** — jalankan quality gate terkecil yang relevan.
5. **Build clean** — hapus output lama lalu jalankan `python run_pipeline.py`.
6. **Reconcile** — bandingkan database, JSON outputs, notebook, dan CLI.
7. **Handoff** — isi `workpapers/DELIVERY_REVIEW.md` dan serahkan evidence review.

## Commands
```bash
python preflight.py
python quality_checks/01_environment.py
python quality_checks/02_schema.py
python quality_checks/03_master.py
python quality_checks/04_relations.py
python quality_checks/05_full_pipeline.py
python run_pipeline.py
python validate_delivery.py
```

Untuk Windows, lihat `WINDOWS_COMMANDS.md`.

## Repository Map
| Path | Peran |
|---|---|
| `PROJECT_BRIEF.md` | Engineering ticket dan acceptance criteria |
| `DATA_CONTRACT.md` | Kontrak input dan aturan integritas |
| `schema.sql` | DDL source of truth |
| `src/warehouse.py` | Koneksi, load policy, dan query API |
| `run_pipeline.py` | Reproducible build entry point |
| `quality_checks/` | Quality gates per tahap |
| `notebooks/` | Review surface untuk evidence |
| `workpapers/` | Design notes, incident evidence, dan sign-off |
| `data/output/` | Generated delivery artifacts; aman untuk dibangun ulang |

## Working Agreement
- Jangan mengedit source data agar test lolos.
- Jangan menaruh business logic hanya di notebook.
- Jangan mengabaikan row gagal; buat kegagalannya terlihat dan dapat dijelaskan.
- Jangan menandai delivery selesai hanya karena happy path berjalan.
