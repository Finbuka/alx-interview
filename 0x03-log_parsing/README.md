
This repository contains a Python script that reads lines from standard input and computes metrics based on the input format.

## Usage

To use the script, you can pipe input from a file or another command into the script using the following command:

python
Copy code
cat input.txt | python metrics.py
Alternatively, you can run the script and then enter input manually:

Copy code
python metrics.py
The script will read input line by line and compute the following metrics:

Total file size: The sum of all previous file sizes.
Number of lines by status code: The number of lines with each possible status code (200, 301, 400, 401, 403, 404, 405, and 500).
The script will print these metrics after every 10 lines of input and when the user interrupts the script with CTRL + C. The final metrics will be printed when the script finishes reading input.

Input format
The script expects input lines to be in the following format:

php
Copy code
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
If a line does not match this format or contains invalid values, it will be skipped.

Implementation
The script is implemented in Python and uses the following libraries:

sys for reading input from standard input.
collections.defaultdict for counting the number of lines for each status code.
The script starts by defining an empty list and a dictionary to store the file sizes and status codes, respectively. It then enters a loop that reads each line from standard input, parses the values, and updates the metrics. After every 10 lines, the script prints the metrics computed so far.

If the user interrupts the script with CTRL + C, the KeyboardInterrupt exception is caught and the script ends. Finally, the script prints the final metrics.
