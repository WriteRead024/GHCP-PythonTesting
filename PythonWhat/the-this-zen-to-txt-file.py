
# Feb. 21, 2024
# Rich W.

# pretty much directly from
# https://stackoverflow.com/a/30942680


import sys

old_stdout = sys.stdout
sys.stdout = open('out.txt', 'w')

import this

sys.stdout.close()

sys.stdout = old_stdout