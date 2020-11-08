# The Main CLI Interface For Alfred
from alfred import *
import sys
from misc import *
import time
import os

github_link = "https://github.com/alfred-python/Alfred"

# Print the alfed banner/logo
def show_banner(show_face=True):
    if show_face:
        print("""                                                                                      
                                      CaqCrrJwhhQ<                                                       
                                   df!i!!!!iliil||/(ho.                                                  
                                .al!ii!!!!!!!!!!i!|||//zh.                                               
                              .biii!!!!!!!!!!!!!!!!!(((|()k, .                                           
                             ,dl!!!!!!!!!!!!!!!!!!!!!(|(((|1a                                            
                           .+f!!!!!!!!!!!!!!!!!!!!!!!!(((((((0?.                                         
                           `v!!!!!!!!!!!!!!i!!!!!!!!!!~(((((((|Z                                         
                           k!!!!!!!!!!!!!!!!!!!!!!!!!!!(((((((()p                                        
                          r!!!!!!!!!!!!!!!!n!!!!!!!!!!!(((((((((/C                                       
                          ki!!!!!!!!!!!!!!i!u!!!!!!!!!-(((|()(((|h.                                      
                         !/!!!!!!!!!!!!!!i!iJl!!t0moahwn)||((a)(|/v                                      
                     d Z.Ll!!!!!!!!ii!irdhaOxxl!<l!!>il(((((((((((h                                      
                   "q aq(hli!!!!!!ii!!!!!!!!iai!!bl!!!!kkhhhr)(|((a#  ~q`    .                           
                   ..o~`.hli!!!!!!ih<!!![nnr]Q?Xkbhdqa((((((()Q|((h k,a1 jkn^                            
               >JmkhY O Jhli!!!!!!i!!!!l!iiii!0>!lp!i?(|((((((((((hC,'k`k v^                             
                  w   k *Oli!!!!Ji!!!!!!!!!!!!L>!it_!iC(((((((((((/a.k h`Q z                             
               h !   U;^a-Z!!!!!lm/!!!!!!!!!!!!b!iiU-i!m((((((((0|((h`k| h."                             
               v '. ." ho h!i!!!!!l|k1i!i!!!!!i!ai>+{x!a(((((((h(((|q .     ?hkv                         
               `> ;0 l  k k!i!!!!iiiiiICaI!!!!!i>?i)<alo((((()z|()||)    <b{(b)Y^                        
              o' `   )  d,/[!!!!!!!i!_klk;f!!!Qi|+k>q(|xkkkkkp((()k Ik)|hf(|)k                        
               U    h|  >j`v!!!Uhhhzkobkkrk :Ckkp}bqhban0_N` fdLbkhYa|(nd|((((b                        
                   /..o` J??!!lliit   hkkbh'o(k)|aliaAiscool 0 b))wkq(|dY((((((|/                       
                  .a    .da!!!![kmY{/      k)v)>!!!!!ilhbkf)`,z_h|))pL)bf(|((((()0                       
                        'k!il+ikaiokc!ukb!Zh-iI:k_kil!!lk} (---]_ka(/a()((((((((fv                       
          lo**pOv_"     `0i!!Zi-qlit(!ii|df :;;;;k!i!ii>ia,1vjz})f|(|Uv(((((((((h                        
          0l!l<)z[il!_doal!!!ii!ii!ii!||mbv ;I:;;a!!!!!<>!a--?]+k|((((d|((|(||(d,                        
          _/(((((((((xt!!il!!!!!!!!!!!!!0k/;,X:;Z!!!i!!i|iikhbZ((((((babt(tqkkX                          
         !_|((((((((((((({Oii!!!!!!!!!!iQi!khpaU~bi!!!!!{[!J|Q/(((((hd                                   
         `Y)|((((((((((((((uwii!!!!!!!!iZ!<bl!!!!!~!!!!!1(iq((a((()kU                                    
           .p(1|(((((((((|(||0w!!i!!!!!i0ia!Z?ll!!!!!!!i|{!h(|h(((pU                                     
              qr((((|(/wQ[I'`!l!h{ii!!!iJ!i!ilpOliii!!!>(!!h(k)((|k+                                     
                 "+,           +liCL!!!ij!i!!!iiiZh_i!!--!vZb|((a(uQ                                     
                                +!i>k>l!tli!i!!!!!!!!+h~!!h({|(|)j)w>>>aO.                               
                                 (!i!!!i{i!!iiii!!!ii!!i}<i!{|((aa/U<>>>>ca                              
                                  bi!!i!]<!InlYIx!i>i!Jdakt>ll~/ObQ1,::>>>~aJ                            
                                   Jli!!>-!!!kipxhhk}!</|(]iiii((((vh:,l>>>>ik                           
                                   .I-!!!1l!ilbbkdi!||_i!!(i1>z|(((|)Q::>>>>i>k;dz                       
                                 "Z,I,m>!)<bhkkz!!!!!!!!>)Cjh{p((((|(d::;>>>>>>kI .coZ                   
                                 h:::,,ai(i!!hlii!!!!!_(()(1{!1(((((|h,::>>>>>>:a                        
                                 h:::::I(ci!!i!!!!!!!+>!!i!!!!!i(|(|fQ;::>>>>>>i                         
                                 p,:::::,k!ii!!!!!!!!!!!!!!!!!!!>(((h,:;l>>>>>ii                         
                                :~,:::::,ka!!!!!!!!!!!!!!!!!!!!!i|(h;:::>>>>>><{                         
                                O,:::::::a:,k!iii!!!!!!!!!!!!!!!!|Uu:::;<>>>>>>>`                        
                                h::::::::k::,,au!i!!!!!!!!!!!!!!!qv[dJaO<>>>>>>--                        
                             a" p::::::::X::::::}k}!iiiii!!!!!rk_rb a 1_ a|i>>>+?                        
                            a   -x:::::::/,:::::;:,,bhkhhkh*n.0hd .a o'uz. k>>>1]                        
                           k      k,:::::<"::::::::;::,,ak}h ), 1^ .p.o  p< a>i0'                        
                                   d+,;::l,::::::::,,hbb L ^' b  O. w  kk"   dck                         
                                    ^*I,:,+::::::::,k ha  [ C. k  d, k`       d1                         
                                      Yv:;L;:::::::hh.o.~.o Z. O<!a+                                     
                                        q(h;:::::::k I/Z^ b;nkk_+.                                       
                                         .hb:^::::,*   '                                                 
                                          m ,a-":;:a                                                     
                                          (.   IU,:!1
                                            """)
    print(f"""
                         ___  _  ___             _ 
                        | . || || | '_ _  ___  _| |
                        |   || || |-| '_>/ ._>/ . |
                        |_|_||_||_| |_|  \___.\___|.py
                        --> Python Instagram Account Bruteforcer
                        --> github: {github_link}
    """)

# Return input from the user and exit on a keybaord interrupt
def get_answer():
    try:
        return input('[alf]>')
    except KeyboardInterrupt:
        error('\n[EXIT] Keyboard Interrupt Exiting...', fatal=True)

# Show Help
def show_help():
    print("\t\t--- Alfred Help ---")
    print('set          Set <value> <variable>, change value of a variable eg, set verbose false')
    print('options      Show the optional variables')
    print("help         Show this help message")
    print('proxies      Downloads Proxies for Alfred')
    print('ready        Get alfred ready for an attack, ready proxies and passwords')
    print('attack       Start the attack and get alfred ready if necessary')
    print('clear        Clear the terminal screen')
    print('reset        Reset variables to default')
    print("banner       Show the epic Alfred banner")

# Show the current setting for Alfred
def show_options(alfred):
    print('\t\t[Options]')
    if alfred.ready:
        good("     ----> Alfred is Ready to Attack! <----")
    else:
        error("               ___Not Ready___")
    print(f"Verbose (print verbose output?)                      ", end=""); show_bool(alfred.verbose)
    print(f"Prompt  (Prompt before more tasks)                   ", end=""); show_bool(alfred.prompt)
    print(f'Mode (attack mode; single/combo)                     {alfred.attack_mode}')
    print(f"ProxyList (proxylist file path)                      ", end=""); show_bool(alfred.proxy_file)
    print(f'ComboList (wordlist file path, NO SPACES)            ', end=""); show_bool(alfred.combolist_path)
    print(f'User (username for single attack)                    {alfred.single_user}')
    if alfred.combos != []:
        print(f"Number Of Combos(length of  combos)                  {len(alfred.combos)}")
    print(f"Store (Write hacked accounts to a file)              ", end=""); show_bool(alfred.store_password)
    print(f"Delay (wait after login try to not get blocked)      {alfred.delay_time}")
    if alfred.store_password:
        print(f'StoreFile (File with hacked accounts)                {alfred.write_path}')

# Evaluate a set answer
def evaluate_answer_set(answer, alfred):
    variable, value = answer.split(" ")[1].strip(), answer.split(" ")[2].strip()
    # Set verbosity
    if variable.lower() in ['verbose', 'verbosity', 'verb']:
        if value not in ['True', 'true', 'false', 'False']:
            error(f"Error, Value \'{value}\' is not a boolean!")
        else:
            alfred.verbose = eval(value.title())

    elif variable.lower() in ['prompt', "check"]:
        if value not in ['True', 'true', 'false', 'False']:
            error(f"Error, Value \'{value}\' is not a boolean!")
        else:
            alfred.prompt = eval(value.title())
            
    # Set delay time
    elif variable.lower() in ['delay', 'sleep', 'delaytime']:
        try:
            float(value) + 1
            if float(value) < 0:
                error("Error: Delay Time cannot be < 0!")
            alfred.delay_time = float(value.strip())
        except ValueError:
            error(f"Error: \'{value}\'is not a number!")

    # Set Attack Mode (single, combo)
    elif variable.lower() in ['attackmode', 'mode', 'attack_mode']:
        if value.lower() not in ['combo', 'single']:
            error(f"Error, Attack Mode \'{value}\' not valid attack mode!")
        else:
            alfred.attack_mode = value       

    # Set Proxy File
    elif variable.lower() in ['proxies', 'proxy_list', 'proxylist', 'plist']:
        alfred.proxy_file = value.replace("\"", "")
        alfred.ready = False

    # Set the Combolist/Wordlist
    elif variable.lower() in ['combolist', 'combos', 'wordlist', 'passlist', 'passwordlist', 'clist', 'wlist']:
        alfred.combolist_path =  value.replace("\"", "")
        alfred.ready = False

    # Set the file to write passwords to 
    elif variable.lower() in ['storef', 'storefile']:
        alfred.write_path = value

    # Set the password list divider, in the case of a weird password list (username:password) where : is hte divider
    elif variable.lower() in ['divider', 'password_divider']:
        alfred.divider = value

    # Set the user in the case of a singular username attack
    elif variable.lower() in ['user', 'singleuser', 'single', 'single_user', 'single_username']:
        alfred.single_user = value
        alfred.ready = False

    elif variable.lower() in ['store', 'storepassword', 'store_password']:
        if value not in ['True', 'true', 'false', 'False']:
            error(f"Error, Value \'{value}\' is not a boolean!")
        else:
            alfred.store_password = eval(value.title())
    # Default case
    else:
        error(f"Error: Set \'{answer.split(' ')[1]}\' not a variable!")

# Check the answer and run a funtion accordingly
def evaluate_answer(answer, alfred):
    if answer.strip() == "":
        return
    if answer in ['help', 'show help', 'show h']:
        show_help()
    elif answer in ['banner', 'show banner', 'show b']:
        show_banner(show_face=alfred.config_data['show_face'])
    elif answer in ['show options', 'settings', 'show settings', 'options', 'option']:
        show_options(alfred)

    # Download Proxies for alfred to use
    elif answer.lower() in ['download_proxies', 'get_proxies', 'getproxies']:
        alfred.download_proxies()
    
    # Ready Alfred for an attack
    elif answer.lower() in ['ready', 'ready_alfred', 'getready', 'get_ready']:
        if alfred.ready:
            print('[READY] Alfred is already ready!')

        elif not alfred.single_user and alfred.combolist_path == "":
            error("Error: Cannot Attack, no combolist specified!")
        elif alfred.single_user and alfred.attack_mode != "single" and alfred.combolist_path == "":
            error("Error: No Combolist specified, did you forget to set mode to single?")

        elif not alfred.single_user and alfred.attack_mode == 'single':
            error("Error: No user specified, cannot get ready!")
        # Ready for a single attack if no wordlist
        else:
            alfred.ready_attack()

    elif answer.strip() in ['attack', 'run', 'hack']:
        if not alfred.single_user and alfred.combolist_path == "":
            error("Error: Cannot Attack, no combolist or attack target username specified!")

        elif alfred.combolist_path == "" and alfred.attack_mode != 'single':
            if alfred.prompt:
                if input("Use single attack mode? (y/n)") in ['yes', 'ye', 'y']:
                    alfred.attack_mode == "single"
            else:
                alfred.attack_mode = 'single'
                print("[AUTO] Set mode to single!")
            print(f"[PASSLIST] No passlist specified, using top {len(alfred.single_pwds)} passwords!")
            for pwd in alfred.single_pwds:
                alfred.combos.append([alfred.single_user, pwd])
            alfred.go()

        elif alfred.single_user and alfred.attack_mode != "single":
            if alfred.prompt:
                if input("Use single attack mode? (y/n)") in ['yes', 'ye', 'y']:
                    alfred.attack_mode == "single"
            else:
                alfred.attack_mode = "single"
                print("[AUTO] Set mode to single!")
        else:
            alfred.go()

    # Set variables to values, by splitting answer
    elif answer.split(" ")[0] == 'set':
        if len(answer.split(" ")) < 3:
            error('Error: Please specify more arguments for set, try: \'set <variable> <value>\'')
        else:
            evaluate_answer_set(answer, alfred)

    elif answer in ['clear', 'cls']:
        clear_screen()

    elif answer in ['reset', 'fullreset']:
        alfred.reset(full=True)
    # Default to an error message on an invalid command
    else:
        error('Error: Command Not Recognised!')

# Main code
def main():
    A = Alfred()
    show_banner(show_face=A.config_data['show_face'])
    while 1:
        answer = get_answer()        
        evaluate_answer(answer, A) 
