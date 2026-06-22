
def extract():
    data = [
        {"id": 1, "name": "Alice", "amount": 100},
        {"id": 2, "name": "Bob", "amount": 200},
        {"id": 3, "name": "Charlie", "amount": 300},
    ]
    return data


def validate(data):
    errors = []
    for row in data:
        if row["amount"] is None:
            errors.append(f"Missing amount for id {row['id']}")
    return errors


def run():
    data = extract()
    errors = validate(data)
    if errors:
        print("DATA QUALITY ISSUES FOUND:")
        for e in errors:
            print(f"  - {e}")
        exit(1)
    else:
        print("All checks passed.")


if __name__ == "__main__":
    run()

## adding some commments