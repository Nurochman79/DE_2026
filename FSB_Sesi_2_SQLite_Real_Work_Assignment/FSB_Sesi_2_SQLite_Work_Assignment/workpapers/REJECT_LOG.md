# Incident Evidence: Rejected Transactions

Gunakan file generated `data/output/rejected_transactions.json` sebagai source of truth. Dokumen ini mencatat analisis, bukan menggantikan log mesin.

| tx_id | user_id | product_id | Database error | Contract violated | Disposition |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

## Triage Notes
- Apakah failure berasal dari data producer, schema, atau load order?
- Apakah row valid setelah failure tetap loaded?
- Apakah reject aman untuk direplay setelah master data diperbaiki?
- Informasi apa yang perlu dikirim ke upstream owner?

## Incident Decision
- [ ] Reject expected; delivery dapat lanjut
- [ ] Unexpected failure; block handoff
