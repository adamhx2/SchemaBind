import pytest
from schemabind import bind


def test_missing_attribute_raises_attribute_error():
    row = bind({"first_name": "Alex"})
    assert row.first_name == "Alex"
    with pytest.raises(AttributeError):
        row.frist_name
