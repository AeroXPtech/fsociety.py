print("------------------")
print("     Index.py     ")
print("    by techx32    ")
print("------------------")

while True:
    print("\n--------------------")
    print("help - show commands")
    print("--------------------")

    choice = input("user@kalilinux~$ ").lower

    if choice == "help":
        print("------------------------")
        print("  neofetch - show spec  ")
        print("  github - show source  ")
        print("  infos - show updates  ")
        print("  exit - exit programm  ")
        print("------------------------")

    elif choice == "neofetch":
        print("""
        user@kali
        ---------
        OS: Kali Linux
        RAM: 8GB (2GB used)
        Storage: 251GB
        CPU: Intel i5
        """)

    elif choice == "github":
        print("\nhttps://github.com/AeroXPtech")

    elif choice == "infos":
        print("\nNew Features Soon")

    elif choice == "exit":
        print("\nGood Bye!")
        break

    else:
        print("\nIllegal Command")