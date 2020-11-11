# Alfred
Pure Python3 Alfred Instagram Bruteforce Tool

Alfred is a python3 made proof of concept showing that Instagram accounts can still be bruteforced in 2020. Alfred is largely object orientated with requests being the core library. I would appreciate sort of feedback on the project, please feel free email me at alfred-python@protonmail.com. Alfred can bruteforce instagram accounts by sending legitimate seeming requests and then checking the response to decide whether it was a successful login. 

**WARNING**
- Alfred is not to be used for any illegal purposes, as stated above it is a proof of concept and may be used in ethical hacking operations.

## Installation
To install Alfred simply open your terminal and run a few commands:
- `git clone https://github.com/alfred-python/Alfred/`
- `cd Alfred`
- `python3 main.py`

## Features
Currently Alfred operates in two modes; single and combo
- Combo: Using a wordlist different account names and passwords 
- Single: Attacking account by only using a single username

## Usage
### Single Mode
-`set user <usernmae>` Set username to attack
-`set combolist <combolist>` Set the Combolist
-`run` This get alfred ready and download proxies then run the attack

## Notes
"alfred.config" can be manually edited if not working as it holds few pieces of data that determines if alfred can run etc.
Alfred has been tested on windows and linux but may need some changes to file io to work on Mac OS. 

### Updates
Alfred is currently in early stages and in the next update i intend to add
- more in config file
- pause/resume attacks
- verbose help/advanced
- creeper attack
- proxy custom location
- user agent customization    
- command line arguments to start attack faster
- Code simplification( there are some ugly nested conditionals)
