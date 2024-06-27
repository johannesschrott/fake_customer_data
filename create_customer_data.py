import random
from faker import Faker
import pandas
from tqdm.contrib.concurrent import process_map
import os

NUMBER_OF_ROWS_TO_GENERATE: int = 10000
SEED: int = 0xCAFE

Faker.seed(SEED)
fake = Faker()
random.seed(SEED)


def create_record(_: int):
    customer: dict = dict()

    if not random.random() < 0.2:
        customer["CustomerID"] = random.randint(0, 99999)
    if not random.random() < 0.2:
        customer["FirstName"] = fake.first_name()
    if not random.random() < 0.2:
        customer["LastName"] = fake.last_name()
    if not random.random() < 0.2:
        customer["AddressID"] = random.randint(0, 99999)
    if not random.random() < 0.2:
        customer["EmailAddress"] = fake.safe_email()
    if not random.random() < 0.2:
        customer["Phone"] = fake.phone_number()
    if not random.random() < 0.2:
        customer["Mobile"] = fake.phone_number()
    return customer


def main():
    customers: list

    customers = process_map(
        create_record,
        range(0, NUMBER_OF_ROWS_TO_GENERATE),
        max_workers=os.cpu_count(),
        chunksize=10,
    )

    df = pandas.DataFrame(customers)
    df = df.set_index("CustomerID")
    df.to_csv("fake_customer_data.csv")


if __name__ == "__main__":
    main()
