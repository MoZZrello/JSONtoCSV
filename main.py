#Made by: Richard Harman
#Date: 14.3.2022

import urllib.request
import json
import pandas as pd
import os
import sys

def getParams():
    if len(sys.argv) == 3:
        mode = sys.argv[1]
        json_path = sys.argv[2]
        return mode, json_path
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-h" or sys.argv[1] == "-help":
            help()
        else:
            wrongArg()
    else:
        wrongArg()

def wrongArg():
    print("Wrong parameters. Use:\n"
          " main.py -h\n"
          " or\n"
          " main.py -help\n"
          "for more information.\n")
    exit(1)

def help():
    print("This is script for translating JSON to CSV format.\n"
          "Usage:\n"
          "  main.py [mode] [path to JSON file]\n"
          "Modes:\n"
          "  -u   =   takes url address as second parameter and gets JSON data from this adress.\n"
          "  -f   =   takes path to a file in computer as second parameter and gets JSON data from this file.\n"
          "Path:\n"
          "  If you are in -u mode -> path should be url in 'http://address.com/JSON' format.\n"
          "  If you are in -f mode -> path should be in computer file 'C:/User/data.json' format.\n")
    exit(0)


mode, json_path = getParams()

if mode == "-u":
    with urllib.request.urlopen(json_path) as url:
        data = json.loads(url.read().decode())
    arg = json.dumps(data)
elif mode == "-f":
    arg = json_path
else:
    wrongArg()

df = pd.read_json(arg)
if os.path.exists("./data.csv") and os.stat("./data.csv").st_size != 0:
    df.to_csv('./data.csv', mode="a", encoding='utf-8', index=False, header=False)
else:
    df.to_csv('./data.csv', mode="w", encoding='utf-8', index=False, header=True)

exit(0)
