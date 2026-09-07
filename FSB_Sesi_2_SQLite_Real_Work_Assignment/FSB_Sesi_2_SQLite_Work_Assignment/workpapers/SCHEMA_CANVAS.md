# Design Record: Warehouse Schema

Isi sebelum implementasi atau saat keputusan berubah.

## Proposed Model
| Decision | Choice | Reason / risk controlled |
|---|---|---|
| Grain `users` | | |
| Grain `products` | | |
| Grain `transactions` | | |
| PK `users` | | |
| PK `products` | | |
| PK `transactions` | | |
| FK user | | |
| FK product | | |
| `NOT NULL` fields | | |
| `CHECK` constraints | | |
| Load order | | |
| Transaction boundary | | |

## Design Review
- Apakah model mencegah duplicate business keys?
- Apakah transaction fact dapat berdiri tanpa master reference?
- Constraint mana yang mencegah silent corruption?
- Apa konsekuensi bila insert row ke-10 gagal?
- Apakah schema aman untuk rebuild?

## Decision
- [ ] Approved for implementation
- [ ] Needs revision

Reviewer / date:
