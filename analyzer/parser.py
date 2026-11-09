def parse_log_line(line):
    parts = line.split()

    if len(parts) != 7:
        return None

    try:
        status = int(parts[6])

        if status < 100 or status > 599:
            return None

        log_entry = {
            "date": parts[0],
            "time": parts[1],
            "level": parts[2],
            "ip": parts[3],
            "method": parts[4],
            "url": parts[5],
            "status": status
        }

        valid_levels = ["INFO", "WARNING", "ERROR", "CRITICAL"]
        if parts[2] not in valid_levels:
            return None

        return log_entry

    except ValueError:
        return None