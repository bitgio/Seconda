import argparse
import sys
import string
import matplotlib.pyplot as plt
import time

t_initial = time.time()
object = argparse.ArgumentParser()
object.add_argument("file", type = argparse.FileType('r', encoding= 'UTF-8-sig'), help = "This will be the book for the counting")
args = object.parse_args()

il_file = args.file.read().replace('\n', '').replace(' ', '')
il_file = il_file.translate(str.maketrans('', '', string.punctuation))

count = {}
alf = list(string.ascii_lowercase)

for letter in alf:
    count[letter] = 0

counter = 0
    
for letter in il_file:
    if letter.lower() in alf:
        count[letter.lower()] += 1
        counter += 1
    
count = {k: ((v / counter) * 100) for k, v in count.items()} 

t_final = time.time()
elapsed_time = t_final - t_initial
print(f'The program lasts {elapsed_time}s to run.')

print(count)

plt.hist(count.values())
plt.show()
