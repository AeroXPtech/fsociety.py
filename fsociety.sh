#!/bin/bash

# 1. Check ob Python vorhanden ist
if ! command -v python3 &> /dev/null
then
    echo "PYTHON NOT FOUND PLEASE INSTALL PYTHON"
    exit 1
fi

echo "EXECUTING SCRIPT PLEASE WAIT"

# 2. Countdown in einer Zeile (3... 2... 1...)
for i in {3..1}
do
   echo -n "$i... "
   sleep 1
done

echo -e "\nStarting Python script..."

# 3. Das Skript ausführen
python3 fsociety.py
