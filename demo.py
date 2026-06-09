import csv
from schemabind import bind


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
