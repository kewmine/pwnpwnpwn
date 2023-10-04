#!/bin/bash

# prep for setup
LOG="/root/env/main.log"

echo "cd $HOME
. /root/env/pyenv/bin/activate
" > /root/.bashrc


function init_script() {
    # update os
    dpkg --configure -a
    apt-get clean
    apt-get update -y
    apt-get upgrade -y

    # setup python for pwning
    apt-get install python3-full python3-setuptools -y
    python3 -m venv /root/env/pyenv
    . ~/.bashrc
    pip install pwntools
}

init_script &> $LOG
clear

# jail info
echo ""
echo -e "\t SETUP COMPLETE "
echo "------------------------------------------"
echo "[*] $(ldd --version | grep -i glib)"
echo "[*] $(python -V)"
echo $(pwn version)
echo -e "to spawn a shell, run:\n\t docker exec -it pwnpwnpwn bash"
echo "------------------------------------------"
