class BoundRow:
    def __init__(self, data):
        self._data = data
        self._normalized_keys = {}

        for key in data.keys():
            normalized_key = key.lower().replace(" ", "_")
            if normalized_key in self._normalized_keys:
                raise ValueError(
                    f"Duplicate normalized key '{normalized_key}' for original keys "
                    f"'{self._normalized_keys[normalized_key]}' and '{key}'"
                )
            self._normalized_keys[normalized_key] = key

    def __getattr__(self, name):
        if name not in self._normalized_keys:
            available_fields = ", ".join(self._data.keys())
            raise AttributeError(
                f"Field '{name}' not found. " f"Available fields: {available_fields}"
            )

        original_key = self._normalized_keys[name]
        return self._data[original_key]

    def __repr__(self):
        return f"BoundRow(keys={list(self._data.keys())})"

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def get(self, key, default=None):
        return self._data.get(key, default)


def bind(data):
    if not isinstance(data, dict):
        raise TypeError(f"Expected dict, got {type(data).__name__}")

    return BoundRow(data)
