#!/usr/bin/env python3

import pyperclip
import time
import sys

# monitor paste buffer
# if paste buffer contains a new url, append it to the urls file

MIN_URL_LEN = 7

filename = "urls.txt" if len(sys.argv) == 1 else sys.argv[1]

# TODO read the last line out of the file when we start
prev_buff = ""
while (True):
    buff = pyperclip.paste()
    if (len(buff) > MIN_URL_LEN and buff != prev_buff and buff.startswith("http")):
        f= open(filename,"a+")
        prev_buff = buff
        f.write("%s\n" % (buff))
        f.close()
    time.sleep(0.4)



