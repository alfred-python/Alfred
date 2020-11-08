# Alfred
Pure Python Alfred Instagram Bruteforce Tool

Alfred is a python made proof of concept showing that Instagram accounts can still be bruteforced in 2020. Alfred is largely object orientated with requests being the core library.
I would appreciate sort of feedback on the project, please feel free email me at alfred-python@protonmail.com

### WARNING ###
- Alfred is not to be used for any illegal purposes, as stated above it is a proof of concept and may be used in ethical hacking operations if desired.

# Features
Currently Alfred operates in two modes; single and combo
- Combo: Using a wordlist different account names and passwords 
- Single: Attacking account by only using a single username

# Notes
Alfred can bruteforce instagram accounts by sending legitimate seeming requests and then checking the response to decide whether it was a successful login.
While I realise that I could of made Alfred in one file and largely simplified the command line ui, i decided to adopt a similar style to metasploit because I enjoy it and new features can more easily be implemented.

# Updates
Alfred is currently in early stages and in the next update i intend to add
- more in config file
- pause/resume attacks
- verbose help/advanced
- creeper attack
- proxy custom location
- user agent customization    
- command line arguments to start attack faster
