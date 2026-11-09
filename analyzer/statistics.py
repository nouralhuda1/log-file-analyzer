from collections import Counter


def count_log_levels(logs):
    levels = [log["level"] for log in logs]
    return Counter(levels)


def count_status_codes(logs):
    statuses = [log["status"] for log in logs]
    return Counter(statuses)


def get_top_ips(logs):
    ips = [log["ip"] for log in logs]
    return Counter(ips).most_common(5)


def count_requests(logs):
    successful = 0
    failed = 0

    for log in logs:
        if 200 <= log["status"] < 400:
            successful += 1
        elif log["status"] >= 400:
            failed += 1

    return successful, failed

def filter_by_level(logs, level):
    return [
        log for log in logs
        if log["level"].upper() == level.upper()
    ]


def filter_by_ip(logs, ip_address):
    return [
        log for log in logs
        if log["ip"] == ip_address
    ]


def filter_by_status(logs, status_code):
    return [
        log for log in logs
        if log["status"] == status_code
    ]
