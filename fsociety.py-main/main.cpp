#include "fsociety.h"

int main() {

    std::srand(std::time(0)); // IMPORTANT für Random

    Fsocity::banner();

    std::string choice;

    while (true) {

        std::cout << "\n┌──(fsociety㉿kali)\n└─$ ";
        std::cin >> choice;

        if (choice == "help") Fsocity::help();
        else if (choice == "fastfetch") Fsocity::fastfetch();
        else if (choice == "github") Fsocity::github();
        else if (choice == "infos") Fsocity::infos();
        else if (choice == "ddos") Fsocity::ddos();
        else if (choice == "hack") Fsocity::hack();
        else if (choice == "ransom") Fsocity::ransom();
        else if (choice == "bruteforce") Fsocity::bruteforce();
        else if (choice == "exit") break;
        else std::cout << "Illegal Command\n";
    }

    return 0;
}