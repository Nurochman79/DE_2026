# Acceptance Baseline — Reviewer Reference

Dokumen ini adalah baseline verifikasi, bukan langkah implementasi. Engineer bebas memilih struktur internal selama contract dan acceptance criteria terpenuhi.

## Expected Business Results
- users: **14**
- products: **10**
- accepted transactions: **22**
- rejected transactions: **3**
- revenue: **8.745.000**
- top products: **P006/Webcam 19**, **P008/Notebook 2**, **P007/Desk Lamp 1**

## Quality Gate Signals
```text
PASS {'users', 'products', 'transactions'} 2
PASS 22 22 3
READY FOR REVIEW
```

## Failure Triage
| Symptom | First checks |
|---|---|
| counts benar, revenue salah | join condition, duplicate join, aggregation grain |
| reject count bukan 3 | PRAGMA, FK DDL, load order, rollback scope |
| notebook lolos, CLI gagal | hidden state, working directory, stale import, hard-coded data |
| rerun gagal duplicate key | cleanup/idempotency policy |
| semua transactions rollback | transaction boundary terlalu lebar |

## Evidence Standard
Angka tanpa command dan artifact yang dapat direproduksi belum dianggap evidence. Reviewer harus dapat menjalankan build dari output directory kosong dan mendapatkan hasil yang sama.
