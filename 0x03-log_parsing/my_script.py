#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys
import signal

total_file_size = 0
stat_cod_cnt = {}
line_num = 0

def signal_handler(sig, frame):
    """Define a function to handle keyboard interrupts"""
    print_stats()
    sys.exit(0)


def print_stats():
    """Define a function to print the current stats"""
    print(f"File size: {total_file_size}")
    for status_code in sorted(stat_cod_cnt.keys()):
        print(f"{status_code}: {stat_cod_cnt[status_code]}")

for line in sys.stdin:
    line_num += 1

    try:
        ip_address, _, _, _, _, _, _, status_code, file_size = line.split()
        status_code = int(status_code)
        file_size = int(file_size)
    except ValueError:
        continue

    total_file_size += file_size
    stat_cod_cnt[status_code] = stat_cod_cnt.get(status_code, 0) + 1

    if line_num % 10 == 0:
        print_stats()

signal.signal(signal.SIGINT, signal_handler)
"""handle signal"""
