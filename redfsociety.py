import time
import sys
import hashlib
from tqdm import tqdm

# Red Colors
RED = "\033[91m"
BOLD_RED = "\033[1;91m"
RESET = "\033[0m"

def print_red(text):
    print(f"{RED}{text}{RESET}")

def print_bold_red(text):
    print(f"{BOLD_RED}{text}{RESET}")

def progress_bar(task, duration=4):
    print_red(f"[*] {task}")
    for _ in tqdm(range(30), 
                  bar_format=f"{RED}{{l_bar}}{{bar}}{RESET}{{r_bar}}", 
                  ncols=70, 
                  leave=True):
        time.sleep(duration / 30)
    print()

# Banner
print_red("""
    .o88o.                               o8o                .
    888 `"                               `"'              .o8
   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
    888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
    888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
   o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
                                                                .o...P'
                                                                `XER0'
     """)

while True:
    print(f"{RED}─" * 65 + RESET)
    print_red("   help        → Show commands")
    print_red("   fastfetch   → Show system specs")
    print_red("   github      → Show source")
    print_red("   infos       → Show updates")
    print_red("   ddos        → DDoS attack")
    print_red("   hack        → Payload hack")
    print_red("   bruteforce  → Bruteforce attack")
    print_red("   exit        → Exit program")
    print(f"{RED}─" * 65 + RESET)

    print(f"{RED}┌──(fsociety㉿kali)-[~]{RESET}")
    choice = input(f"{RED}└─$ {RESET}").strip().lower()

    if choice == "help":
        print_red("\nAvailable commands:")
        print_red("   help, fastfetch, github, infos, ddos, hack, bruteforce, exit\n")

    elif choice == "fastfetch":
        print_red("""
        ..............                                      fsociety@kali
             ..,;:ccc,.                              ---------------------------
           ......''';lxO.                            OS: Kali GNU/Linux Rolling x86_64
 .....''''..........,:ld;                            Host: 20W1S7PR18 (ThinkPad T14 Gen 2i)
            .';;;:::;,,.x,                           Kernel: Linux 6.18.12+kali-amd64
       ..'''.            0Xxoc:,.  ...               Uptime: 2 hours, 11 mins
   ....                ,ONkc;,;cokOdc',.             Packages: 3568 (dpkg)
  .                   OMo           ':ddo.           Shell: zsh 5.9
                     dMc               :OO;          Display (AUO323D): 1920x1080 in 14", 60 Hz [Built-in]
                     0M.                 .:o.        DE: Xfce4 4.20
                     ;Wd                             WM: Xfwm4 (X11)
                      ;XO,                           WM Theme: Kali-Dark
                        ,d0Odlc;,..                  Theme: Fusion [Qt], Kali-Dark [GTK2/3/4]
                            ..',;:cdOOd::,.          Icons: Flat-Remix-Blue-Dark [Qt], Flat-Remix-Blue-Dark [GTK2/3/4]
                                     .:d;.':;.       Font: Cantarell (11pt) [GTK2/3/4]
                                        'd,  .'      Cursor: Adwaita (24px)
                                          ;l   ..    Terminal: qterminal 2.3.0
                                           .o        Terminal Font: FiraCode (10pt)
                                             c       CPU: 11th Gen Intel(R) Core(TM) i5-1145G7 (8) @ 4.40 GHz
                                             .'      GPU: Intel Iris Xe Graphics @ 1.30 GHz [Integrated]
                                              .      Memory: 2.06 GiB / 15.33 GiB (13%)
                                                     Swap: 0 B / 12.30 GiB (0%)
                                                     Disk (/): 93.97 GiB / 220.63 GiB (43%) - ext4
                                                     Local IP (wlan0): 192.168.178.35/24
                                                     Battery (5B10W51826): 100% [Discharging]
                                                     Locale: nl_NL.UTF-8
                                                     0x10 0x20 0x30 0x40 0x50 0x60 0x67

                                                                              
                                                                             
        """)

    elif choice == "github":
        print_red("\n→ https://github.com/AeroXPtech")

    elif choice == "infos":
        print_red("\n[+] Red design activated with progress bars")

    elif choice == "exit":
        print_bold_red("\n[!] Good Bye! Stay safe.")
        sys.exit(0)

    elif choice == "ddos":
        site = input(f"{RED}Target website (ex. usa.gov): {RESET}") or "usa.gov"
        print_red(f"\n[*] Attacking {site} with Mira Botnet (1.7M devices)...")
        progress_bar("Sending attack packets", 8)
        print_bold_red(f"\n[+] Attack finished! {site} → 503 Service Unavailable")

    elif choice == "hack":
        ip = input(f"{RED}Target IP (ex. 129.983.38.723): {RESET}") or "129.983.38.723"
        print_red("\nAvailable Payloads:")
        print_red("   1 - Luma3DS")
        print_red("   2 - Ja1lh4ck1ng")
        print_red("   3 - dualpayload")
        print_red("   4 - payload.cia")
        print_red("   5 - Custom exploit")
        payload = input(f"{RED}Choose payload >>> {RESET}") or "1"

        print_red(f"\n[*] Injecting {payload} into {ip}...")
        progress_bar("Loading payload", 4)
        progress_bar("Patching kernel", 5)
        progress_bar("Injecting exploit", 6)
        progress_bar("Rebooting target", 4)
        print_bold_red(f"\n[+] Successfully hacked {ip}!")

    elif choice == "bruteforce":
        target_hash = "6f52550186105d6a2f7c006769062947"
        passwords = [
            "123456", "password", "123456789", "qwerty", "admin", "root", "letmein",
            "fsociety", "elliot", "kali", "hacker", "shadow", "123123"
        ]

        print_bold_red(f"[!] BRUTEFORCE ATTACK STARTED ON HASH: {target_hash}")
        print()

        found = False
        for pwd in tqdm(passwords, bar_format=f"{RED}[*] Trying: {{desc}}{RESET}", ncols=70):
            print(f"    {pwd.ljust(15)}", end="\r")
            time.sleep(0.55)
            if hashlib.md5(pwd.encode()).hexdigest() == target_hash:
                print_bold_red(f"\n\n[+] PASSWORD FOUND: {pwd}")
                found = True
                break

        if not found:
            print_bold_red("\n[-] Attack failed. Password not in dictionary.")

    else:
        print_red("[-] Illegal Command. Type 'help' for commands.")

    time.sleep(0.8)