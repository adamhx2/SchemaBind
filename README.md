# SchemaBind

SchemaBind reduces repetitive mapping boilerplate by exposing existing schema fields as readable Python attributes.

Instead of:

```python
first_name = row.get("first_name")
email = row.get("email")
address = row.get("address")
```

Use:

```python
row = schemabind.wrap(row)

row.first_name
row.email
row.address
```

SchemaBind does not create schemas, validate data, transform values, or make decisions. It simply provides a cleaner way to access fields that already exist.
