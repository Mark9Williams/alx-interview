#!/usr/bin/env python3
""" A script that reads stdin line by line and computes metrics """

import sys
import signal
import re

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
file_total_size = 0
line_count = 0
log_format = re.compile(r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

def print_statistics():
    """Prints the statistics of the log"""
    print(f'File size: {file_total_size}')
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print(f'{key}: {status_codes[key]}')

def handle_interruption(signal, frame):
    """Handles the interruption signal (ctrl + c)"""
    print_statistics()
    sys.exit(0)

# Set signal handler
signal.signal(signal.SIGINT, handle_interruption)

try:
    for line in sys.stdin:
        match = log_format.match(line.strip())
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))

            file_total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1 

            line_count += 1
            if line_count % 10 == 0:
                print_statistics()

except Exception as e:
    print(f"Exception: {e}", file=sys.stderr)

# Print final statistics
print_statistics()
