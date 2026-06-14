import csv
from schemabind import bind


def get_sample_csv():
    return "samples/csv/customer.csv"


def read_csv(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        return list(reader)


def run_demo():
    csv_path = get_sample_csv()
    rows = read_csv(csv_path)

    customer = bind(rows[0])

    print(customer)
    print(customer.first_name)
    print(customer.email_address)
    print(customer.phone_number)
    print(customer.get("signup_source"))
    print(customer.keys())


def main():
    run_demo()


if __name__ == "__main__":
    main()
