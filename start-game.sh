#!/bin/bash

# this bash script is for simplifying the interface for GuessWord game.
# please run 'bash start-game.sh' for starting the script

cd src_files
pip install -r requirements.txt
python guessword_full.py
