# Wordle Solver

This solver is a program to help you play and win at Wordle.

## How to use the software
Create a folder called data with the command `mkdir data`.

Download a dictionnaries in the languages which you are interested in. For instance:
- for English: `wget https://raw.githubusercontent.com/dwyl/english-words/master/words.txt -O english_dict` from dwyl
- for French: `wget https://raw.githubusercontent.com/hbenbel/French-Dictionary/master/dictionary/dictionary.txt -O french_dict`

Apply preprocessing on the file with the command `python3 preprocessing.py data/your_dict.txt`

Use the repository with a python notebook for instance.