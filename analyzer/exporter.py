import csv
import json


def export_to_csv(logs, file_path):
    if not logs:
        print("No data available to export.")
        return

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        fieldnames = logs[0].keys()

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(logs)

    print(f"CSV report saved to {file_path}")


def export_to_json(logs, file_path):
    if not logs:
        print("No data available to export.")
        return

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(logs, file, indent=4)

    print(f"JSON report saved to {file_path}")
