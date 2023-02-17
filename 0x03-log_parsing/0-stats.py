#!/usr/bin/python3
"""
reading stdin
"""

import sys
import signal


def signal_handler(sig, frame):
    """Define a function to handle keyboard interrupts"""
    print_stats()
    sys.exit(0)

# Register the interrupt signal handler
signal.signal(signal.SIGINT, signal_handler)

# Initialize the stats variables
total_file_size = 0
status_code_counts = {}


def print_stats():
    """Define a function to print the current stats"""
    print(f'Total file size: {total_file_size}')
    for status_code in sorted(status_code_counts.keys()):
        print(f'{status_code}: {status_code_counts[status_code]}')

# Read from stdin line by line
line_num = 0
for line in sys.stdin:
    line_num += 1

    # Parse the line
    try:
        ip_address, _, _, _,_,_,_,status_code, file_size = line.split()
        status_code = int(status_code)
        file_size = int(file_size)
    except ValueError:
        # Skip the line if it doesn't match the expected format
        continue

    # Update the stats
    total_file_size += file_size
    status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

    # Print the stats every 10 lines
    if line_num % 10 == 0:
        print_stats()

# Print the final stats
print_stats()
