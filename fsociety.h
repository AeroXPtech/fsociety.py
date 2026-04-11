#ifndef FSOCIETY_H
#define FSOCIETY_H

#include <iostream>
#include <string>
#include <thread>
#include <chrono>
#include <cstdlib>
#include <ctime>

class Fsocity {
public:

    static void banner() {
        std::cout << R"(
    .o88o.                               o8o                .
    888 ""                               `"'              .o8
   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
    888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
    888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
   o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
                                                                .o...P'
                                                                `XER0'
)" << std::endl;
    }

    static void help() {
        std::cout <<
        "\nhelp - show commands\n"
        "fastfetch\ngithub\ninfos\nexit\nddos\nhack\nransom\nbruteforce\n";
    }

    static void fastfetch() {
        std::cout <<
        "\nOS: Kali Linux (sim)\nCPU: Intel i5\nRAM: 16GB\nGPU: Intel Iris Xe\n";
    }

    static void github() {
        std::cout << "\nhttps://github.com/AeroXPtech\n";
    }

    static void infos() {
        std::cout << "\nfsociety simulator updated\n";
    }

    static void ddos() {
        std::string site;
        std::cout << "Website: ";
        std::cin >> site;

        for (int i = 0; i < 10; i++) {
            std::this_thread::sleep_for(std::chrono::milliseconds(300));
            std::cout << "DDoSing " << site << " ... 200 OK\n";
        }

        std::cout << "DDoS finished (simulation)\n";
    }

    static void hack() {
        std::string ip;
        std::cout << "Target IP: ";
        std::cin >> ip;

        std::string payload;
        std::cout << "Payload ID: ";
        std::cin >> payload;

        std::cout << "\nInjecting...\n";
        std::this_thread::sleep_for(std::chrono::seconds(1));

        std::cout << "Loading kernel...\n";
        std::this_thread::sleep_for(std::chrono::seconds(1));

        std::cout << "Rebooting...\n";
        std::this_thread::sleep_for(std::chrono::seconds(2));

        std::cout << "[✓] Hacked (simulation): " << ip << "\n";
    }

    static void ransom() {
        std::cout << "\n!!! FILES ENCRYPTED !!!\n";

        for (int i = 10; i >= 0; i--) {
            std::cout << "Time left: " << i << "s\n";
            std::this_thread::sleep_for(std::chrono::seconds(1));
        }
    }

    static void bruteforce() {

        std::string passwords[] = {
            "123456", "password", "123456789", "qwerty", "12345678", "12345", "1234567", "password123", "1234567890", "1234",
            "admin", "p@ssword", "root", "111111", "monkey", "sunshine", "iloveyou", "letmein", "secret", "football",
            "dragon", "master", "shadow", "hunter", "superman", "batman", "killer", "matrix", "hacker", "fsociety",
            "welcome", "login", "guest", "access", "system", "security", "server", "network", "firewall", "database",
            "000000", "123123", "654321", "987654321", "password1", "pass123", "abc123", "qazwsx", "wsxedc", "edcrfv",
            "chelsea", "arsenal", "liverpool", "united", "barcelona", "madrid", "soccer", "baseball", "basketball", "hockey",
            "charles", "george", "thomas", "william", "alexander", "nicholas", "matthew", "andrew", "daniel", "robert",
            "jennifer", "jessica", "michelle", "amanda", "ashley", "sarah", "stephanie", "heather", "nicole", "elizabeth",
            "princess", "angel", "sweetie", "honey", "cookie", "maggie", "charlie", "bailey", "lucky", "buster",
            "laptop", "computer", "keyboard", "monitor", "iphone", "android", "windows", "linux", "ubuntu", "kali", "elliot",
            "alderson", "elliotalderson", "verstappen"
        };

        int size = sizeof(passwords) / sizeof(passwords[0]);

        std::cout << "[*] Brute force starting...\n";

        int success = rand() % size;

        for (int i = 0; i < 100; i++) {

            std::string attempt = passwords[rand() % size];

            std::cout << "Trying: " << attempt << "\n";
            std::this_thread::sleep_for(std::chrono::milliseconds(100));

            if (i == success) {
                std::cout << "\n[+] MATCH FOUND: " << attempt << "\n";
                return;
            }
        }

        std::cout << "[-] No match found\n";
    }
};

#endif