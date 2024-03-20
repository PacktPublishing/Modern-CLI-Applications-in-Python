#!/usr/bin/env python3

import sys

try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    total = num1 + num2

    print(f'The sum is: {total}')

except ValueError as e:
    sys.stderr.write(f'Error: {e}\n')
