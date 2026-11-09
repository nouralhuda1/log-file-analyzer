
from analyzer.reader import read_log_file
from analyzer.parser import parse_log_line

from analyzer.statistics import (
    count_log_levels,
    count_status_codes,
    get_top_ips,
    count_requests,
    filter_by_level,
    filter_by_ip,
    filter_by_status
)

from analyzer.exporter import export_to_csv, export_to_json


# ==================================
# FILTER MENU
# ==================================

def show_filter_menu(parsed_logs):
    print("\n===== LOG FILTER =====")
    print("1. Filter by log level")
    print("2. Filter by IP address")
    print("3. Filter by HTTP status code")
    print("4. Back to main menu")

    choice = input("\nChoose an option: ")

    if choice == "1":
        level = input("Enter log level: ")
        return filter_by_level(parsed_logs, level)

    elif choice == "2":
        ip = input("Enter IP address: ")
        return filter_by_ip(parsed_logs, ip)

    elif choice == "3":
        try:
            status = int(input("Enter HTTP status code: "))
            return filter_by_status(parsed_logs, status)

        except ValueError:
            print("Invalid status code.")
            return []

    elif choice == "4":
        return None

    else:
        print("Invalid option.")
        return []


# ==================================
# EXPORT MENU
# ==================================

def show_export_menu(parsed_logs, filtered_logs):
    print("\n===== EXPORT REPORT =====")
    print("1. Export all logs to CSV")
    print("2. Export all logs to JSON")
    print("3. Export filtered logs to CSV")
    print("4. Export filtered logs to JSON")
    print("5. Back to main menu")

    choice = input("\nChoose an option: ")

    if choice == "1":
        export_to_csv(parsed_logs, "reports/log_report.csv")

    elif choice == "2":
        export_to_json(parsed_logs, "reports/log_report.json")

    elif choice == "3":
        export_to_csv(filtered_logs, "reports/filtered_report.csv")

    elif choice == "4":
        export_to_json(filtered_logs, "reports/filtered_report.json")

    elif choice == "5":
        return

    else:
        print("Invalid option.")


# ==================================
# READ AND PARSE LOG FILE
# ==================================

log_lines = read_log_file("data/sample.log")

parsed_logs = []

for line in log_lines:
    result = parse_log_line(line)

    if result is not None:
        parsed_logs.append(result)


# ==================================
# ANALYZE LOGS
# ==================================

levels = count_log_levels(parsed_logs)
statuses = count_status_codes(parsed_logs)
top_ips = get_top_ips(parsed_logs)
successful, failed = count_requests(parsed_logs)


# ==================================
# MAIN MENU
# ==================================

filtered_logs = []

while True:

    print("\n===== LOG FILE ANALYZER =====")
    print("1. View analysis report")
    print("2. Filter logs")
    print("3. Export reports")
    print("4. Exit")

    choice = input("\nChoose an option: ")

    # View analysis report
    if choice == "1":

        print("\n===== ANALYSIS REPORT =====")

        print("\nTotal log entries:", len(parsed_logs))

        print("\n--- Log Levels ---")
        for level, count in levels.items():
            print(f"{level}: {count}")

        print("\n--- HTTP Status Codes ---")
        for status, count in statuses.items():
            print(f"{status}: {count}")

        print("\n--- Top IP Addresses ---")
        for ip, count in top_ips:
            print(f"{ip}: {count} requests")

        print("\n--- Request Summary ---")
        print("Successful requests:", successful)
        print("Failed requests:", failed)

    # Filter logs
    elif choice == "2":

        result = show_filter_menu(parsed_logs)

        if result is not None:
            filtered_logs = result

            print("\n===== FILTERED RESULTS =====")
            print("Matching entries:", len(filtered_logs))

            for log in filtered_logs:
                print(log)

    # Export reports
    elif choice == "3":

        show_export_menu(parsed_logs, filtered_logs)

    # Exit
    elif choice == "4":

        print("\nExiting Log File Analyzer. Goodbye!")
        break

    else:
        print("\nInvalid option. Please try again.")
