def read_log_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = [line.rstrip("\n") for line in file]

        return lines

    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return []

    except PermissionError:
        print(f"Error: Permission denied: {file_path}")
        return []