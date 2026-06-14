import pytest
from schemabind import bind


def test_attribute_access_returns_value():
    row = bind({"first_name": "Kaladin"})

    assert row.first_name == "Kaladin"


def test_missing_attribute_raises_attribute_error():
    row = bind({"first_name": "Kaladin"})

    with pytest.raises(AttributeError):
        row.frist_name


def test_duplicate_normalized_keys():
    # Ambiguous normalized names are rejected instead of guessed.
    with pytest.raises(ValueError):
        bind({"first_name": "Dalinar", "First Name": "Adolin"})


def test_keys_values_items():
    data = {"first_name": "Dalinar", "last_name": "Kholin"}
    row = bind(data)

    assert set(row.keys()) == set(data.keys())
    assert set(row.values()) == set(data.values())
    assert set(row.items()) == set(data.items())


def test_get_method():
    data = {"first_name": "Shallan", "last_name": "Davar"}
    row = bind(data)

    assert row.get("first_name") == "Shallan"
    assert row.get("last_name") == "Davar"
    assert row.get("non_existent", "bridge_four") == "bridge_four"


def test_non_dict_input():
    with pytest.raises(TypeError):
        bind(["not", "a", "dict"])


def test_normalization():
    # Spaces and case are normalized for attribute access.
    row = bind({"First Name": "Adolin", "Last Name": "Kholin"})

    assert row.first_name == "Adolin"
    assert row.last_name == "Kholin"


def test_get_preserves_original_keys_after_normalization():
    row = bind({"First Name": "Navani"})

    assert row.first_name == "Navani"
    assert row.get("First Name") == "Navani"


def test_keys_preserve_original_names_after_normalization():
    row = bind({"First Name": "Jasnah"})

    assert "First Name" in row.keys()
    assert "first_name" not in row.keys()


def test_empty_string_values_are_valid():
    # Empty strings are real values, not missing fields.
    row = bind({"spren_name": ""})

    assert row.spren_name == ""


def test_duplicate_normalized_key_error_names_conflict():
    # Collision errors name the normalized key and conflicting fields.
    with pytest.raises(ValueError) as error:
        bind({"First Name": "Dalinar", "first_name": "Adolin"})

    message = str(error.value)
    assert "first_name" in message
    assert "First Name" in message


def test_missing_attribute_error_names_available_fields():
    # Missing-attribute errors name the request and available fields.
    row = bind({"ideal": "Life before death"})

    with pytest.raises(AttributeError) as error:
        row.oath

    message = str(error.value)
    assert "oath" in message
    assert "ideal" in message


def test_repr_includes_keys():
    row = bind({"radiant_order": "Windrunner"})

    assert "radiant_order" in repr(row)
