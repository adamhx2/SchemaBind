# SchemaBind

SchemaBind reduces repetitive dictionary lookup boilerplate by exposing existing fields as readable Python attributes.

Instead of:

```python
first_name = row["first_name"]
email = row["email_address"]
phone = row.get("phone_number")
```

Use:

```python
from schemabind import bind

customer = bind(row)

customer.first_name
customer.email_address
customer.phone_number
```

SchemaBind is currently focused on dictionaries, including rows produced by `csv.DictReader`.

It does not create schemas, validate data, transform values, or infer new fields. It simply provides a cleaner way to access fields that already exist.

## Example

```python
import csv
from schemabind import bind

with open("samples/csv/customer.csv") as f:
    rows = list(csv.DictReader(f))

customer = bind(rows[0])

print(customer.first_name)
print(customer.email_address)
print(customer.phone_number)
```

Missing attributes raise `AttributeError` instead of silently returning `None`, which helps catch typos in field names.

## Field Normalization

SchemaBind supports simple field-name normalization for attribute access.

For example:

```python
customer = bind({"First Name": "Kaladin"})

print(customer.first_name)
```

The original dictionary keys are preserved for dictionary-style helpers:

```python
customer.keys()
customer.get("First Name")
```

If multiple fields normalize to the same attribute name, SchemaBind raises `ValueError` instead of guessing which field to use.

For example:

```python
bind({
    "First Name": "Dalinar",
    "first_name": "Shallan",
})
```

Both fields would normalize to `first_name`, so the binding is rejected as ambiguous.
