# Data Contract: Processed Commerce Events

**Contract version:** 1.0  
**Producer:** Upstream processing job  
**Consumer:** SQLite warehouse pipeline

## Entity Grain
| Entity | Satu row merepresentasikan |
|---|---|
| `users` | satu user unik |
| `products` | satu product unik |
| `transactions` | satu transaction line untuk satu user dan satu product |

## `users`
| Field | Type | Required | Constraint / behavior |
|---|---|---:|---|
| `user_id` | TEXT | yes | primary key, unique |
| `name` | TEXT | no | nullable |
| `email` | TEXT | no | nullable |
| `city` | TEXT | no | nullable |

## `products`
| Field | Type | Required | Constraint / behavior |
|---|---|---:|---|
| `product_id` | TEXT | yes | primary key, unique |
| `name` | TEXT | yes | `NOT NULL` |
| `price` | REAL | yes | `NOT NULL`, `CHECK(price >= 0)` |
| `category` | TEXT | no | nullable |

## `transactions`
| Field | Type | Required | Constraint / behavior |
|---|---|---:|---|
| `tx_id` | TEXT | yes | primary key, unique |
| `user_id` | TEXT | yes | FK ke `users.user_id` |
| `product_id` | TEXT | yes | FK ke `products.product_id` |
| `quantity` | INTEGER | yes | `NOT NULL`, `CHECK(quantity > 0)` |
| `tx_date` | TEXT | no | nullable; pipeline tidak mengubah nilainya |

## Referential Integrity Policy
- `transactions.user_id` harus ditemukan pada `users.user_id`.
- `transactions.product_id` harus ditemukan pada `products.product_id`.
- Koneksi wajib mengaktifkan `PRAGMA foreign_keys = ON`; deklarasi FK tanpa enforcement tidak memenuhi kontrak.
- Transaction yang melanggar referensi disebut **orphan transaction**.
- Orphan transaction tidak masuk tabel final dan harus tercatat di reject log.
- Valid transaction lain tetap diproses; tidak boleh hilang karena satu reject.

## Metric Definitions
| Metric | Definition |
|---|---|
| table count | `COUNT(*)` pada masing-masing tabel setelah load selesai |
| revenue | `SUM(transactions.quantity * products.price)` setelah join via `product_id` |
| top products | total `quantity` per product, descending; ambil 3 teratas |

## Compatibility Notes
Perubahan field, type, grain, atau definisi metric adalah contract change. Jangan menebak atau memperluas scope; catat sebagai issue untuk producer/consumer review.
