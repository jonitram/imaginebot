#!/bin/bash

tokenslocation=$PWD/tokens.txt

# create virtual environment
python3.7 -m venv .venv
source ./.venv/bin/activate

# install requirements
python3.7 -m pip3 install -r requirements.txt

buildtokens="n"

if [ -f "$tokenslocation" ]; then
    read -p $'Would you like to delete the old \'tokens.txt\' file and make a new one? [y/n] ' resettokens
    if [ $resettokens == "y" ]; then
        rm tokens.txt
        buildtokens="y"
    fi
else
    buildtokens="y"
fi
if [ $buildtokens == "y" ]; then
    touch tokens.txt
    read -sp $'Please input your Consumer API Key:' c_key
    echo $c_key >> tokens.txt
    read -sp $'\nPlease input your Consumer API Secret Key:' cs_key
    echo $cs_key >> tokens.txt
    read -sp $'\nPlease input your Access Token:' a_token
    echo $a_token >> tokens.txt
    read -sp $'\nPlease input your Access Token Secret:' as_token
    echo $as_token >> tokens.txt
fi

