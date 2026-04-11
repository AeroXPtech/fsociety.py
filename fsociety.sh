#!/bin/bash

clear

echo "
    .o88o.                               o8o                .
    888 \"                               \"'              .o8
   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
    888    d88(  \"8 d88' \`88b d88' \"Y8 \`888  d88' \`88b   888    \`88.  .8'
    888    \"Y88b.  888   888 888        888  888ooo888   888     \`88..8'
    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    \`888'
   o888o   8\"\"888P' \`Y8bod8P' \`Y8bod8P' o888o \`Y8bod8P'   \"888\"      d8'
                                                                .o...P'
                                                                \`XER0'
"

while true; do
    echo ""
    echo "--------------------"
    echo "help - show commands"
    echo "--------------------"

    read -p "┌──(fsociety㉿kali)
└─$ " choice

    case "$choice" in

        help)
            echo "------------------------"
            echo " fastfetch - show specs "
            echo " github - show source  "
            echo " infos - show updates  "
            echo " exit - exit program   "
            echo " ddos - simulation     "
            echo " hack - payload hack   "
            echo " exploit - gain disk   "
            echo " systemd - logs        "
            echo "------------------------"
        ;;

fastfetch)
cat << "EOF"

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

EOF
;;

        github)
            echo "https://github.com/AeroXPtech"
        ;;

        infos)
            echo "added payload hack and ransomware simulator"
        ;;

        exit)
            echo "Good Bye!"
            exit 0
        ;;

        ddos)
            read -p "choose Website: " site
            read -p "Botnet name: " botnet
            echo "Running simulation..."
            for i in {1..10}; do
                echo "DDoSing $site ... 200 OK"
                sleep 1
            done
            echo "Finished! (simulation)"
        ;;

        hack)
            read -p "choose IP: " ip
            read -p "Payload: " payload
            echo "Injecting..."
            sleep 2
            echo "Successfully Hacked $ip!"
        ;;

        exploit)
            read -p "choose Location: " site
            read -p "OS: " os
            read -p "Payload: " payload
            echo "Running exploit..."
            sleep 3
            echo "Successfully Exploited $site"
        ;;

        systemd)
            echo "Loading logs..."
            sleep 2
            echo "########## 100%"
            read -p "Directory: " dir
            echo "Logs saved in $dir"
        ;;

        *)
            echo "Illegal Command"
        ;;

    esac
done