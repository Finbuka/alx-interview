#!/usr/bin/python3
"""
A script: Reads standard input line by line and computes metrics
"""


def signal_handler(sig, frame, total_file_size, stat_cod_cnt):
    """
    Handles the CTRL + c signal
    Args:
        sig (int): total log size after every 10 successfully read line
        frame (FrameType): dictionary of status codes and counts
        total_file_size (int): params for the print stats
        stat_cod_cnt (int): params for the print stats
    """
    print_stats(total_file_size, stat_cod_cnt)
    sys.exit(0)


def print_stats(total_file_size, stat_cod_cnt):
    """
    Prints generated report to standard output
    Args:
        total_file_size (int): total log size after every 10 successfully
        stat_cod_cnt (dict): dictionary of status codes and counts
    """
    print(f"File size: {total_file_size[0]}")
    for status_code in sorted(stat_cod_cnt.keys()):
        print(f"{status_code}: {stat_cod_cnt[status_code]}")


def parse_logs():
    """
    Reads logs from standard input and generates reports
    Reports:
        * Prints log size after reading every 10 lines & at KeyboardInterrupt
    Raises:
        KeyboardInterrupt (Exception): handles this exception and raises it
    """
    total_file_size = [
        0,
    ]
    stat_cod_cnt = {}
    line_num = 0
    new_signal_handler = functools.partial(
        signal_handler,
        total_file_size=total_file_size,
        stat_cod_cnt=stat_cod_cnt,
    )
    signal.signal(signal.SIGINT, new_signal_handler)

    for line in sys.stdin:
        line_num += 1

        try:
            _, _, _, _, _, _, _, status_code, file_size = line.split()
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        total_file_size[0] += file_size
        stat_cod_cnt[status_code] = stat_cod_cnt.get(status_code, 0) + 1

        if line_num % 10 == 0:
            print_stats(total_file_size, stat_cod_cnt)


if __name__ == "__main__":
    import sys
    import signal
    import functools

    parse_logs()
