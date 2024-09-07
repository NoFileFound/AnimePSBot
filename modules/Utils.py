import random

def RandomHEXColor():
    return int(("%06x" % random.randint(0, 0xFFFFFF)), 16)