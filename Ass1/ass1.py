import argparse
import sys
import string
import matplotlib.pyplot as plt
import time

t_initial = time.time()
object = argparse.ArgumentParser()
object.add_argument("file", type = argparse.FileType('r', encoding= 'UTF-8'), help = "This will be the book for the counting")
args = object.parse_args()
#print(args.file.readlines())

il_file = args.file.readlines()
count = {}
alf = list(string.ascii_lowercase)
for letter in alf:
    count[letter] = 0

c = 0
#print(count)
    
for i in range(len(il_file)):
    #print(line)
    il_file[i] = il_file[i].lower()
    il_file[i] = il_file[i].replace('\n', '')
    il_file[i] = il_file[i].lstrip()
    for element in il_file[i]:
        for letter in alf:
            if element == letter:
                c += 1
            count[letter] += c
            c = 0

print(count)
all_letters = 0
for val in count.values():
    all_letters += val

for letter in count:
    count[letter] = (count[letter] / all_letters) * 100

t_final = time.time()
elapsed_time = t_final - t_initial
print(f'The program lasts {elapsed_time}s to run.')

#print(count)
#print(all_letters)

plt.hist(count.values())
plt.show()
