# Engineering Ticket: Build SQLite Transaction Warehouse

**Ticket:** DATA-214  
**Owner:** Data Engineer  
**Priority:** High  
**Status awal:** Ready for Development

## Business Request
Finance membutuhkan sumber data lokal yang konsisten untuk menghitung volume transaksi, revenue, dan produk dengan unit penjualan tertinggi. Dataset upstream sudah dibersihkan secara sintaksis, tetapi sebagian transaksi mungkin merujuk master data yang tidak tersedia.

Jika referensi invalid ikut masuk, angka revenue dapat terlihat valid namun salah. Warehouse harus menjadikan pelanggaran relasi terlihat, menolak row bermasalah, dan menyimpan evidence untuk review.

## Scope
### In scope
- membuat SQLite database dari JSON processed;
- menegakkan PK, FK, `NOT NULL`, dan `CHECK` constraints;
- memuat master data sebelum transaction facts;
- menolak transaction orphan tanpa menggagalkan seluruh batch;
- menghasilkan counts, revenue, dan top products;
- menghasilkan artifacts yang dapat dibangun ulang lewat satu command.

### Out of scope
- memperbaiki source data;
- membuat UI/dashboard;
- mengubah definisi metric;
- memasukkan reject ke tabel produksi;
- menyimpan logic final hanya di notebook.

## Inputs
Input read-only:
- `data/processed/users.json`
- `data/processed/products.json`
- `data/processed/transactions.json`

Kontrak field dan relasi ada di `DATA_CONTRACT.md`.

## Required Deliverables
- `data/output/app.db`
- `data/output/rejected_transactions.json`
- `data/output/query_results.json`
- `data/output/metrics.json`
- implementasi pada `schema.sql`, `queries.sql`, dan `src/warehouse.py`
- evidence review yang terisi pada folder `workpapers/`

## Functional Requirements
1. Setiap koneksi production-path mengaktifkan `PRAGMA foreign_keys = ON`.
2. Schema memiliki tabel `users`, `products`, dan `transactions` sesuai data contract.
3. Insert menggunakan parameter binding, bukan string interpolation.
4. Master data dimuat sebelum transactions.
5. Transactions diproses per row atau dengan mekanisme setara yang mempertahankan auditability per failure.
6. Satu row gagal tidak boleh membatalkan row valid lain.
7. Reject log minimal memuat `tx_id`, key referensi, dan alasan database.
8. Query revenue menggunakan join pada grain transaction line.
9. Build harus idempotent dari sisi output: menjalankan ulang menghasilkan state final yang sama.

## Acceptance Criteria
| Check | Expected |
|---|---|
| Users loaded | 14 |
| Products loaded | 10 |
| Transactions accepted | 22 |
| Transactions rejected | 3 |
| Revenue | 8.745.000 |
| Top 3 by units | P006/Webcam 19; P008/Notebook 2; P007/Desk Lamp 1 |
| Transaction foreign keys | 2 |
| Final validator | `READY FOR REVIEW` |

## Non-Functional Requirements
- Reproducible: reviewer dapat rebuild tanpa state notebook.
- Observable: failure dan counts muncul pada output yang dapat diperiksa.
- Reviewable: keputusan schema dan query bisa ditelusuri ke kontrak.
- Safe: source input tidak dimutasi.

## Reviewer Questions
Reviewer akan meminta Anda menjelaskan:
- risiko bisnis yang dicegah tiap constraint;
- mengapa row tertentu ditolak dan row lain tetap committed;
- join condition dan grain revenue;
- bukti bahwa hasil bukan produk dari hidden notebook state;
- cara rollback atau rebuild jika output corrupt.
