def get_int_input(prompt, min_value=None, max_value=None):
    """Prompt user until they enter a valid integer within optional bounds."""
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or \
               (max_value is not None and value > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_float_input(prompt, min_value=None, max_value=None):
    """Prompt user until they enter a valid float within optional bounds."""
    while True:
        try:
            value = float(input(prompt))
            if (min_value is not None and value < min_value) or \
               (max_value is not None and value > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def print_table(data, headers):
    """
    Pretty print a list of dicts or objects as a table.
    data: list of dicts or objects
    headers: list of column headers (and keys if dicts)
    """
    
    widths = []
    for h in headers:
        col_width = max(len(str(h)), *(len(str(row[h])) if isinstance(row, dict) else len(str(getattr(row, h))) for row in data))
        widths.append(col_width)

    
    header_row = " | ".join(str(h).ljust(w) for h, w in zip(headers, widths))
    print(header_row)
    print("-" * len(header_row))

    
    for row in data:
        row_str = []
        for h, w in zip(headers, widths):
            val = row[h] if isinstance(row, dict) else getattr(row, h)
            row_str.append(str(val).ljust(w))
        print(" | ".join(row_str))

def confirm(prompt="Are you sure? (y/n): "):
    """Ask user for yes/no confirmation, return True if yes."""
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "yes"):
            return True
        elif ans in ("n", "no"):
            return False
        else:
            print("Please enter 'y' or 'n'.")
