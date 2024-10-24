#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics """

import signal
import sys
import re

# Dictionary to track status codes and total file size
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
file_total_size = 0
line_count = 0

# Log line format regular expression
log_format = re.compile(
    r'^\S+ - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)


def print_statistics():
    """Prints the statistics of the log"""
    global file_total_size, status_codes
    print(f"File size: {file_total_size}")
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print(f"{key}: {status_codes[key]}")


def handle_interruption(signal, frame):
    """Handles the interruption signal (CTRL + C)"""
    print_statistics()
    sys.exit(0)


# Set signal handler
signal.signal(signal.SIGINT, handle_interruption)

try:
    for line in sys.stdin:
        # Strip whitespace from the line and match with regex
        match = log_format.match(line.strip())
        if match:
            # Extract status code and file size
            status_code = int(match.group(2))
            file_size = int(match.group(3))

            # Update file size and status code count
            file_total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

            # Increment line count and print statistics every 10 lines
            line_count += 1
            if line_count % 10 == 0:
                print_statistics()
except KeyboardInterrupt:
    print_statistics()  
    sys.exit(0)

except Exception as e:
    print(f"Exception: {e}", file=sys.stderr)

# Print final statistics when done
print_statistics()
