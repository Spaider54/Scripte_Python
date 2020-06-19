'''
[+]##################################################################[+]
[+]         @auteur : Walid MENGHOUR                                 [+]
[+]         @Description : Finding Sentences from 2 to n word        [+]
[+]                           with a specific length of first word   [+]
[+]                            and last and frequency                [+]
[+]                                                                  [+]
[+]         @Last Edit : 12/06/2020 - 18:45                          [+]
[+]##################################################################[+]
'''

import re
import sys
import os


# Validation File
if (not os.path.isfile(sys.argv[1]) or not sys.argv[1].endswith(".txt")):
    print("[+]>>"+"\t" * 2 + "FILE NOT FOUND Error")
    print("[+]>>"+"\t" * 2 + "Verify name of text File ")
    exit(0)

# Open File
file_ = open(sys.argv[1], 'r', encoding="utf-8")
# Create File
Results = open("resproject.txt", 'w', encoding="utf-8")


# Read Content
text = file_.readlines()
list_tokens = []
Dic_tokens = {}

# Define Fun


def tokens(table):

    while (table != []):
        # Declaring Variables

        try:
            len_co = int(table[0])
            freq_co = int(table[1])
            lenfirst = int(table[2])
            lenlast = int(table[3])

        except IndexError as e:
            print("[-]"+"\t"*3+"Error"+"\t"*3+"[-]")
            print("\t Problem Number of Entres  ")
            exit(0)
        except ValueError as v:
            print("[-]"+"\t"*3+"Error"+"\t"*3+"[-]")
            print("\tVerify if You Entre a Character in position of number  ")
            exit(0)
        # verify  condition > 2
        if (int(table[0]) <= 1 or int(table[1]) <= 1):
            print("#" * 27 + " Erorr  " + "#" * 27)
            print("\t"*2+"Problem condition range of tokens or frequency")
            exit(0)

        for sentence in text:
            # Extract words
            a = re.split("\W+", sentence.lower())
            # Create tuples
            l = zip(*(a[i:] for i in range(len_co)))

            for j in l:
                # Frequency
                Dic_tokens[j] = Dic_tokens.get(j, 0) + 1

        for k in sorted(Dic_tokens):
            if Dic_tokens.get(k) == freq_co and len(k[0]) == lenfirst and len(k[-1]) == lenlast:
                l = " ".join(k) + " [Frequency : " + \
                    str(Dic_tokens.get(k)) + "]"
                if l not in list_tokens:  # pass dublicate
                    list_tokens.append(l)

        # Clear all sentens in Dictionary
        Dic_tokens.clear()
        # Remove the first 4 argements
        del table[0:4]


# Call Fucntion

tokens(sys.argv[2:])

# Print and save Resaults
for i, j in enumerate(list_tokens, 1):
    print(f"{i} : {j}")
    Results.write(f"{i} : {j}\n")


# Close the File
file_.close()
