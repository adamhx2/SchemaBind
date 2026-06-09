import csv


class BoundRow:
    def __init__(self, data):
        self._data = data

    def __getattr__(self, name):
        if name not in self._data:
            raise AttributeError(
                f"Field '{name}' not found. Available fields: {', '.join(self._data.keys())}"
            )
        return self._data[name]

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


def get_sample_csv():
    # CSV sample paths:
    # samples_csv = "samples/csv/contact_fields.csv"
    # samples_csv = "samples/csv/customer.csv"
    samples_csv = "samples/csv/orders.csv"
    # samples_csv  = "samples/csv/product.csv"
    # samples_csv = "samples/csv/weird_names.csv"

    return samples_csv


def read_csv(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        return list(reader)


def test():
    csv_path = get_sample_csv()
    customer_data = read_csv(csv_path)

    for row in customer_data[1:2]:
        x = bind(row)
        print(x)

        print(x.keys())

        print(x.values())

        print(x.items())

        print(x.first_n)


def main():
    test()


if __name__ == "__main__":
    main()
