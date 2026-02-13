# Inventory Management API

Manajemen API untuk Gudang

## Bahasa
- Python
- FastAPI
- Git branching workflow

## Simulasi Error
commit yang salah sengaja dibuat untuk mensimulasikan kesalahan produksi.

Perbaikan diterapkan menggunakan `git revert` untuk menjaga kebenaran riwayat commit.

## Installation

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

API will run at `http://127.0.0.1:8001`

---

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/items` | List all items |
| GET | `/items/{id}` | Get item by ID |
| POST | `/items` | Create new item |
| PATCH | `/items/{id}` | Update item (partial) |
| DELETE | `/items/{id}` | Delete item |

---

## Item Schema

```json
{
  "id": 1,
  "name": "Laptop",
  "stock": 10,
  "price": 999.99,
  "category": "electronics"
}
```

---

## Example Usage

**Create item**
```bash
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "name": "Laptop", "stock": 10, "price": 999.99, "category": "electronics"}'
```

**Filter by category**
```bash
curl http://localhost:8000/items?category=electronics
```

---

## Changelog

### v1.1.0
- Add `price` and `category` field
- Add `GET /items/{id}` endpoint
- Add filter by category
- Switch `PUT` to `PATCH` for partial update
- Proper HTTP error responses

### v1.0.0
- Initial release
- Basic CRUD endpoints
- Stock negative validation

