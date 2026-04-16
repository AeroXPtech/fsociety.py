require 'time'
require 'digest'

puts <<~BANNER
    .o88o.                               o8o                .
    888 `"                               `"'              .o8
   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
    888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
    888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
   o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
                                                                .o...P'
                                                                `XER0'
BANNER

loop do
  puts "\n--------------------"
  puts "help - show commands"
  puts "--------------------"

  print "┌──(fsociety㉿kali)\n└─$ "
  choice = gets.chomp.downcase.strip

  if choice == "help"
    puts "\n------------------------"
    puts "  fastfetch - show specs  "
    puts "   github - show source   "
    puts "   infos - show updates   "
    puts "   exit - exit program    "
    puts "   ddos - ddos attack     "
    puts "   hack - payload hack    "
    puts " bruteforce - brute force "
    puts "--------------------------"

  elsif choice == "fastfetch"
    puts <<~SPECS
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
    SPECS

  elsif choice == "github"
    puts "\nhttps://github.com/AeroXPtech"

  elsif choice == "infos"
    puts "added payload hack and ransomware simulator"

  elsif choice == "exit"
    puts "\nGood Bye!"
    exit(0)

  elsif choice == "ddos"
    print "choose Website (ex. usa.gov): "
    site = gets.chomp

    puts "\nGood, which botnet do you want to use?"
    puts "Mira (1.7M devices)"
    puts "Ikai (764K devices)"
    puts "Yuro (567K devices)"
    puts "Liro (387K devices)"
    print "→ "
    botnet = gets.chomp

    puts "\nGreat! wait while #{botnet} is doing their work! (Est. 30sec-2min)"
    sleep(2)

    15.times do
      puts "DDoSing #{site}. 200 OK"
      sleep(2)
    end

    puts "\nDDoS finished! 503 Service Unavailable"
    sleep(2)

  elsif choice == "hack"
    print "\nchoose IP (ex. 129.983.38:723 ): "
    ip = gets.chomp

    puts "\nGood, what Payload do you want to use?"
    puts "1 - Luma3DS"
    puts "2 - Ja1lh4ck1ng"
    puts "3 - dualpayload"
    puts "4 - payload.cia"
    puts "5 - Choose own exploit"
    print ">>> "
    payload = gets.chomp

    puts "\nGreat! wait while #{payload} is Injecting The Hack (Est ca 1 min)"
    sleep(5)
    puts "Starting Hack"
    sleep(2)
    puts "loading Payload"
    sleep(2)
    puts "loading Kernel"
    sleep(5)
    puts "patching kernel"
    sleep(2)
    puts "Injecting Payload"
    sleep(5)
    puts "rebooting..."
    sleep(10)
    puts "finishing Hack"
    sleep(6)
    puts "Successfully Hacked #{ip}!"

  elsif choice == "bruteforce"
    common_passwords = [
      "123456", "password", "123456789", "qwerty", "12345678", "12345", "1234567", "password123",
      "admin", "root", "letmein", "welcome", "monkey", "dragon", "master", "shadow", "fsociety",
      "elliot", "alderson", "kali", "hacker", "123123", "qwerty123", "abc123", "password1",
      "111111", "1234", "superman", "batman", "killer", "matrix", "secret", "football"
    ]

    target_hash = "6f52550186105d6a2f7c006769062947"

    puts "\e[1;33m[!] INITIALIZING BRUTE FORCE ATTACK ON HASH: #{target_hash}\e[0m"
    sleep(1)

    found = false

    common_passwords.each do |password|
      print "\r\e[1;34m[*] TRYING:\e[0m #{password.ljust(15)}"
      $stdout.flush

      sleep(rand(0.3..0.8))

      guess_hash = Digest::MD5.hexdigest(password)

      if guess_hash == target_hash
        puts "\n\n\e[1;32m[+] MATCH FOUND!\e[0m"
        puts "\e[1;32m[+] PASSWORD:\e[0m #{password}"
        found = true
        break
      end
    end

    puts "\n\e[1;31m[-] ATTACK FAILED: Password not in dictionary.\e[0m" unless found

  else
    puts "\nIllegal Command"
  end
end