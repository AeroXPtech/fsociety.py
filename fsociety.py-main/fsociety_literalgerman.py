import sys, time, random, hashlib, tkinter
from tkinter import Tk
def ausfuehren(de_code):
    v = {
        'drucke': 'print', 'eingabe': 'input', 'Klasse': 'class', 'beenden': 'exit',
        'warte': 'time.sleep', 'Wahr': 'True', 'wenn': 'if', 'selbst': 'self',
        'niedriger': 'lower', 'initiieren': '__init__', 'ansonsten_wenn': 'elif',
        'importieren': 'import', 'Definition': 'def', 'als': 'as', 'während': 'while',
        'ansonsten': 'else', 'für': 'for', 'schreibe': 'write', 'spülen': 'flush',
        'zufällig': 'random', 'passwort': 'password', 'enkodieren': 'encode',
        'hexverdauen': 'hexdigest', 'zurückkehren': 'return', 'wurzel': 'root',
        'titel': 'title', 'konfigurieren': 'configure', 'etikett': 'label',
        'expandieren': 'expand', 'Etikett': 'Label', 'schriftart': 'font'
    }
    python_code = de_code
    for de in sorted(v.keys(), key=len, reverse=True):
        python_code = python_code.replace(de, v[de])
    
    exec(python_code)

mein_deitscher_code = r'''

drucke("FGESELLSCHAFT")

drucke("\n---------------------")
drucke("hilfe - zeige Behfele")
drucke("---------------------")
    
während Wahr:

    wahl = eingabe("""┌──(fgesellschaft㉿kali)
└─$ """).niedriger()

    wenn wahl == "hilfe":
        drucke("\n---------------------------------------------------------")
        drucke("             schnellesbringen - zeigt Infos               ")
        drucke("                 idiotnabe - zeige Quelle                 ")
        drucke("              infos - zeige Aktualisierungen              ")
        drucke("               beende - beende das Programm               ")
        drucke("verteiltedienstverweigerung - Verteilte Dienstverweigerung")
        drucke("          rohegewalt - Rohe Gewalt Simulator              ")
        drucke("----------------------------------------------------------")

    ansonsten_wenn wahl == "schnellesbringen":
        zeilen: [
"        ..............                                      fgesellschaft@kali",
"             ..,;:ccc,.                              ---------------------------",
"           ......'';lx0                              OS: Kali GNU/Linux Rollend x86_64",
" .....''..........,:ld;                              Gastgeber: 20W1S7PR18 (DenkUnterlage T14 Gen 2i)",
"            .';;;:::;,,.x,                           Kernel: Linux 6.18.12+kali-AMD64",
"       ..''.            OXxoc:,.  ...                Betriebszeit: 2 Stunden, 11 Minuten",
"   ....                ,ONkc;,;cokOdc',.             Packete: 3568 (dpkg)",
"  .                   OMo           ':ddo.           Hülle: zsh 5.9",
"                     dMc               :OO;          Display (AUO323D): 1920x1080 in 14Inch, 60 Hz [Eingebaut]",
"                     0M.                 .:o.        DE: Xfce4 4.20",
"                     ;Wd                             WM: Xfwm4 (X11)",
"                      ;XO,                           WM Thema: Kali-Dunkel",
"                        ,d0Odlc;,..                  Thema: Fusion [Qt], Kali-Dunkel [GTK2/3/4]",
"                            ..',;:cdOOd::,.          Symbole: Flach-Remix-Blau-Dunkel [Qt], Flach-Remix-Blau-Dunkel [GTK2/3/4]",
"                                     .:d;.':;.       Schriftart: Cantarell (11pt) [GTK2/3/4]",
"                                        'd,  .'      Mauszeiger: Adwaita (24px)",
"                                          ;l   ..    Terminal: qterminal 2.3.0",
"                                           .o        Terminal Schriftart: FiraCode (10pt)",
"                                             c       CPU: 11th Gen Intel(R) Kern(TM) i5-1145G7 (8) @ 4.40 GHz",
"                                             .'      GPU: Intel Iris Xe Grafik @ 1.30 GHz [Integriert]",
"                                              .      Arbeitsspeicher: 2.06 GiB / 15.33 GiB (13%)",
"                                                     Austausch: 0 B / 12.30 GiB (0%)",
"                                                     Scheibe (/): 93.97 GiB / 220.63 GiB (43%) - ext4",
"                                                     Lokale IP (wlan0): 192.168.178.35/24",
"                                                     Batterie (5B10W51826): 100% [Entladen]",
"                                                     Lokale: nl_NL.UTF-8",
                 ]
        für zeile in zeilen:
            drucke(zeile)

    ansonsten_wenn wahl == "idiotnabe":
        drucke("\nhttps://github.com/AeroXPtech")

    ansonsten_wenn wahl == "infos":
        drucke("Deutsche Version? (Aus Spaß, wird vielleicht keine Aktualisierungen kriegen)")

    ansonsten_wenn wahl == "beenden":
        drucke("\nTschüss")
        beende()

    ansonsten_wenn wahl == "verteiltedienstverweigerung":
       drucke("Webseite auswählen (z.B. deine.mutter)")
       Seite = eingabe()
       drucke("Perfekt, wart während " + Seite + "Eine VDV Attacke kriegt")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(2)
       drucke("VDVe " + Seite + ". 200 OK")
       warte(5)
       drucke("VDV ist fertig. 503 Service Unverfügbar")
       warte(2)

    ansonsten_wenn wahl == "rohegewalt":

        Definition simulieren_rohe_gewalt(ziel_hash):
            herkömmliche_passwörter = [
            "123456", "password", "123456789", "qwerty", "12345678", "12345", "1234567", "password123", "1234567890", "1234",
            "admin", "p@ssword", "root", "111111", "monkey", "sunshine", "iloveyou", "letmein", "secret", "football",
            "dragon", "master", "shadow", "hunter", "superman", "batman", "killer", "matrix", "hacker", "fsociety",
            "welcome", "login", "guest", "access", "system", "security", "server", "network", "firewall", "database",
            "000000", "123123", "654321", "987654321", "password1", "pass123", "abc123", "qazwsx", "wsxedc", "edcrfv",
            "chelsea", "arsenal", "deine mutter", "liverpool", "united", "barcelona", "madrid", "soccer", "baseball", "basketball", "hockey",
            "charles", "george", "thomas", "william", "alexander", "nicholas", "matthew", "andrew", "daniel", "robert",
            "jennifer", "jessica", "michelle", "amanda", "ashley", "sarah", "stephanie", "heather", "nicole", "elizabeth",
            "princess", "angel", "sweetie", "honey", "cookie", "maggie", "charlie", "bailey", "lucky", "buster",
            "laptop", "computer", "keyboard", "monitor", "iphone", "android", "windows", "linux", "ubuntu", "kali", "elliot",
            "alderson", "elliotalderson", "verstappen", "hamilton", "starwars", "avengers", "pokemon", "superstar", "Nuttööö", "freedom", "awesome",
            "keyboard", "asdfghjk", "mnbvcxz", "1q2w3e4r", "password!", "P@ssw0rd1", "user1234", "test1234", "SSIO", "admin123", "manager",
            "spring2024", "summer24", "winter25", "january", "monday", "coffee", "whiskey", "tequila", "beer123", "smoke",
            "quantum", "entropy", "algorithm", "localhost", "127.0.0.1", "sysadmin", "database1", "oracle", "cisco123", "security!",
            "beowulf", "ragnarok", "anubis", "zeus123", "olympus", "viking", "sparta", "gladiator", "phoenix", "valhalla",
            "carpediem", "mementomori", "cogitoergo", "fortuna", "virtue", "justice", "liberty", "victory", "champion", "winner"
        ]

            drucke(f"\033[1;33m[!] INITIIERE ROHE GEWALT ATTACKE AUF HASH: {ziel_hash}\033[0m")
            warte(1)

            für passwort in herkömmliche_passwörter:
                sys.stdout.schreibe(f"\r\033[1;34m[*] VERSUCHE:\033[0m {passwort:<15}")
                sys.stdout.spülen()
                
                warte(zufällig.uniform(0.3, 0.8))
                
                rate_hash = hashlib.md5(passwort.enkodieren()).hexverdauen()
                
                wenn rate_hash == ziel_hash:
                    drucke(f"\n\n\033[1;32m[+] ÜBEREINSTIMMUNG GEFUNDEN!\033[0m")
                    drucke(f"\033[1;32m[+] PASSWORT:\033[0m {passwort}")
                    zurückkehren
            
            drucke(f"\n\033[1;31m[-] ATTACKE GESCHEITERT: Passwort nicht in der Liste.\033[0m")

        ziel = "6f52550186105d6a2f7c006769062947" 
        simulieren_rohe_gewalt(ziel)
        
    ansonsten:
        drucke("\nHalten sie sich an die Liste")
        
'''
ausfuehren(mein_deitscher_code)
