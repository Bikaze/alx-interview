#!/usr/bin/python3

"""
This script reads log data from standard input and calculates statistics on the log entries.

The script counts the occurrences of different HTTP status codes and calculates the total file size.

Usage: ./0-generator.py | ./0-stats.py
"""

import sys

status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
status_counts = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 1 and parts[-2] in status_codes:
            status = parts[-2]
            size = int(parts[-1])
            total_size += size
            status_counts[status] += 1
            line_count += 1

        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_counts.keys()):
                if status_counts[code] > 0:
                    print("{}: {}".format(code, status_counts[code]))

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))
