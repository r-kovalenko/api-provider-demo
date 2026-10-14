# Customer API changelog

## 2.0.0

Breaking change: `GET /customers/{customer_id}` now returns `full_name` instead of `name`. The old `name` field is removed. The `id` field remains an integer.

## 1.0.0

Returns a synthetic customer with `id` and `name`. Only customer `1` exists; other identifiers return HTTP 404.
