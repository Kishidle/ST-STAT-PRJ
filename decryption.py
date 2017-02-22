import math
import operator
text_cipher = []

#reading text file and putting it to list
with open("textcipher.text") as fileobj:
    for line in fileobj:
        for ch in line:
            text_cipher.append(ch) #we can replace this so that it already counts the frequency of the letter maybe?


#initialization of frequency distribution of letters
#make a list for the frequency distribution, then make a look-up list for the letters?
freq_distrib = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024,
                0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.024, 0.002, 0.020, 0.001]


look_up = [None] * 27
freq_table = [None] * 27
a = 97

#use chr(num) to change 97 into a
for x in range(27):
    look_up.append(a)
    a += 1

#finds the frequency count of each letter in the text_cipher
for ch in text_cipher:
    for x in look_up:
        if look_up[x] = ord(ch):
            freq_table[x] += 1

#bruteforce method: find the largest value of freq_table, which is the most frequent character. find its index and then compare with freq_distrib
index, value = max(enumerate(freq_table), key=operator.itemgetter(1))
#algorithm for frequency analysis goes here








#additional steps goes here(dictionary attacks in case the first attempt fails)
