
#Feb. 2024
#Rich W.

import sys

already_checked = False

def version_check():
    global already_checked
    if (already_checked):
        return
    else:
        print("versioncheck.py")
        print("current Python version:", sys.version)
        if sys.version_info.major != 3 or sys.version_info.minor != 12:
            raise Warning("This script was written for Python 3.12(.1)")
        else:
            print("Python version is the expected 3.12")
        already_checked = True
