#Version 3 - ASSIGNMENT 1 of BASIC PYTHON

#Importing all the libraries required
import argparse
import string
import matplotlib.pyplot as plt
import time
import numpy as np

#To calculate the execution timing
t_initial = time.time()

#Creating the argparse object - The order of the arguments in the command line is the same as how we are about to define each of them
#Remember that to show all the arguments and the corresponding description just type in the command line: python ass1.py -h
object = argparse.ArgumentParser()
object.add_argument("skip", nargs= '?', type = bool, default= False, help = "Type 'True' before the text file to skip the parts of the text that do not pertain to the book (only valid for English books from the Gutenberg Project).")
object.add_argument("file", type = argparse.FileType('r', encoding= 'UTF-8-sig'), help = "Type in the text file of the book you want to analyze.")
object.add_argument("stats", nargs= '?', type = bool, default= False, help = "Type 'True' after the text file in order to print out the number of characters, words and sentences in the whole book")

#Creating the argparse.Namespace object
args = object.parse_args()

#Reading the file as a string, without any '\n', whitespace or capital letter
il_file = args.file.read().replace('\n', '').replace(' ', '')
il_file = il_file.lower()

#Conditional to activate the first skipping argument or not depending on the first boolean input in the command line
if args.skip == True:
    #In this case, the 'skip' argument is activated so we have to shorten the string leaving out the preamble and license
    #We have seen that every book from the Gutenberg Project starts and ends the plain book with a line that always starts as '***', we take that to shorten it
    il_file = il_file[il_file.index('***'):il_file.rfind('***')]
    il_file = il_file.translate(str.maketrans('', '', string.punctuation))
else:
    #In the default case, or if it's consciously activated as 'False', we only remove the punctuation from the string
    il_file = il_file.translate(str.maketrans('', '', string.punctuation))

#Initializing the dictionary with all the alfabet. This variable will later on contain the counting of each letter
count = {}
alf = list(string.ascii_lowercase)
for letter in alf:
    count[letter] = 0
c = 0
all_letters = 0
for element in il_file:
    if element in alf:
        count[element] += 1
        all_letters += 1


#Calculating finally the relative frequency of each letter as a %
rel_freq = {new_k : (val / all_letters)*100 for new_k, val in count.items()}

#We define another argparse.Namespace object with the same input
#It is necessary to define it again because we need to count all the lines 
#and right now the initial input is completely transformed as a long string without any whitespaces or full stops
out_stats = object.parse_args()

#With readlines() we can directly obtain the book as a line-by-line list of arrays
il_file2 = out_stats.file.readlines()

if out_stats.stats == True: #The following code is executed if the final argument 'stats' is activated
    print(f'The number of characters in the book is {all_letters}.')
    counting_words = 0
    for line in il_file2:
        counting_words += len(line.split())
    print(f'The number of words in the book is {counting_words}.')
    print(f'The number of lines in the book is {len(il_file2)}.')

''' This is the prove, the reason why we need to define again another argparse.Namespace object with the initial input. Uncommentate it to see the difference
It looks as if the initial input has been completely transformed and now we can't access it to count the lines & words
if args.stats == True:
    il_file2 = args.file.readlines()
    print(f'The number of characters in the book is {all_letters}.')
    counting_words = 0
    for line in il_file2:
        counting_words += len(line.split())
    print(f'The number of words in the book is {counting_words}.')
    print(f'The number of lines in the book is {len(il_file2)}.')'''


#Printing out the total executing time
t_final = time.time()
elapsed_time = t_final - t_initial
print(f'The program lasts {elapsed_time} s to run.')

#Printing out the histogram with the relative frequency of each letter
plt.hist(rel_freq.values())
plt.xticks(ticks = np.arange(26), labels=rel_freq.keys())
plt.xlabel('Letters of the English alfabet')
plt.ylabel('Relative frequency')
plt.title('Count of the relative frequency of the letters in the book')
plt.show()