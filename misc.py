# Miscellaneuos functions
from termcolor import colored
import subprocess
import time
import json
import os 

# Name of config file
config_name = "alfred.json"

# Error function, can stop the program
def error(msg, fatal=False):
    print(colored(msg, "red"))
    if fatal:
        exit()

# Print in green
def good(msg, ending=False):
    if ending:
        print(colored(msg, "green"), end="")
    else:
        print(colored(msg, "green"))

# Clear the screen
def clear_screen():
    if os.name == "nt":
        os.system('cls')
    elif os.name == "posix":
        os.system('clear')
    else:
        error(f'Error: Cannot clear os name \'{name}\' not recognised!')
        
# Show a boolean with colour
def show_bool(b):
    if not b:
        error(b)
    elif b == "":
        error("None")
    else:
        good(b)

# Read Config File and return dictionary object
def read_config():
    try:
        d = open(str(__file__).replace("misc.py", config_name))
        return json.load(d)
    except FileNotFoundError:
        error(f"Error: Config file not found, make sure {config_name} in directory with alfred files!", fatal=True)

# Write values to config file
def write_config(var, value):
    raw_data = read_config()
    raw_data[var] = value
    with open(str(__file__).replace("misc.py", config_name), 'wt') as f:
        json.dump(raw_data, f, indent=4)
        f.close()

# install required libraries on first run
def run_install():
    print("[INSTALL] Installing Libraries...")
    libs = ["colorama", "termcolor", "proxyscrape"]
    for l in libs:
        os.system("pip install " + l)
    write_config("installed", True)
    good("[INSTALL] Libraries Installed!?")
    clear_screen()