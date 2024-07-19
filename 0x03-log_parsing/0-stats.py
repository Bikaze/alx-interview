#!/usr/bin/python3

"""
This script reads log data from standard input and calculates statistics on the log entries.

The script counts the occurrences of different HTTP status codes and calculates the total file size.

Usage: ./0-generator.py | ./0-stats.py
"""

import sys
import re

# Initialize variables
status_counts = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
total_size = 0
line_count = 0

def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys(), key=int):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

try:
    for line in sys.stdin:
        # Check if the line matches the expected format
        match = re.match(r'\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)', line)
        if match:
            status_code, file_size = match.groups()
            total_size += int(file_size)
            if status_code in status_counts:
                status_counts[status_code] += 1
            line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    # print("Program interrupted by user. Continuing...")
    # Optionally, continue listening for more input or handle as needed