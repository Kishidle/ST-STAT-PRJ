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
sorted_freq = [0.127, 0.091, 0.082, 0.075, 0.070, 0.067, 0.063, 0.061, 0.060, 0.043, 0.040, 0.028, 0.028,
               0.024, 0.024, 0.022, 0.020, 0.020, 0.019, 0.015, 0.010, 0.008, 0.002, 0.002, 0.001, 0.001]
sorted_letters = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p',
                  'b', 'v', 'k', 'j', 'x', 'q', 'z']
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

#bruteforce method?: find the largest value of freq_table, which is the most frequent character. find its index and then compare with freq_distrib
index, value = max(enumerate(freq_table), key=operator.itemgetter(1)) #this finds the largest value in the list and its index

char = look_up[index]
for x in range(27):
    if char < chr(sorted_letters[x]): #this means that we can't subtract to get the shift value since it goes way past z and loops back
        #logic for this should be here
    else: #if not...then we can subtract normally to get the shift value
        shift_value = chr(sorted_letters[x]) - chr(char)

#shift to e going left, do this until you exhaust every letter in the freq_table. this is one option

#less bruteforce method: comparing most common in text to most common in table, 2nd most common in text to 2nd most common in table, and so on...

#find a way to ignore the values already used in the freq_table








#additional steps goes here(dictionary attacks in case the first attempt fails)
