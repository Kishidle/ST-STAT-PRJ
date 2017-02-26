import math
import operator
text_cipher = []

#reading text file and putting it to list
with open("textcipher.txt") as fileobj:
    for line in fileobj:
        for ch in line:
            text_cipher.append(ch) #we can replace this so that it already counts the frequency of the letter maybe?

class Char_Class:
    def __init__(self, char, count):
        self.char = char
        self.count = count

#initialization of frequency distribution of letters
#make a list for the frequency distribution, then make a look-up list for the letters?
freq_distrib = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024,
                0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.024, 0.002, 0.020, 0.001]
sorted_freq = [0.127, 0.091, 0.082, 0.075, 0.070, 0.067, 0.063, 0.061, 0.060, 0.043, 0.040, 0.028, 0.028,
               0.024, 0.024, 0.022, 0.020, 0.020, 0.019, 0.015, 0.010, 0.008, 0.002, 0.002, 0.001, 0.001]
sorted_letters = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p',
                  'b', 'v', 'k', 'j', 'x', 'q', 'z']
look_up = []
shifted_text = []

a = 97
shift_value = 0

freq_table = [None] * 26

#use chr(num) to change 97 into a
for x in range(26):
    look_up.append(a)
    char_test = Char_Class(a, 0)
    freq_table[x] = char_test
    a += 1

#finds the frequency count of each letter in the text_cipher
for ch in text_cipher:
    for x in range(len(look_up)):
        if look_up[x] == ord(ch):
            freq_table[x].count += 1
            #freq_table[x] += 1 old method

print ("What method would you like to use? [1] Bruteforce Method [2] Less BruteForce Method")
#ask for input

#bruteforce method?: find the largest value of freq_table, which is the most frequent character. find its index and then compare with freq_distrib

freq_table.sort(key = operator.attrgetter('count'), reverse=True) #this finds the largest value in the list and its index

print freq_table[0].count

char = freq_table[0].char

for x in range(26):
    sorted_char = ord(sorted_letters[x])
    if char < sorted_char: #this means that we can't subtract to get the shift value since it goes way past z and loops back
        #logic for this should be here
        #increment until equal, loop back to a if it goes past z
        while True:
            if sorted_char != char:
                shift_value += 1
                if chr(sorted_char) == 'z':
                    sorted_char = 97
                else:
                    sorted_char += 1
            else:
                break
    else: #if not...then we can subtract normally to get the shift value
        shift_value = sorted_char - char


    print "Letter " + chr(ord(sorted_letters[x])) + " compared with " + chr(char) + " has shift value of " + str(shift_value)

    #shift the text!


#shift to e going left, do this until you exhaust every letter in the freq_table. this is one option

#less bruteforce method: comparing most common in text to most common in table, 2nd most common in text to 2nd most common in table, and so on...

#algorithm 2
freq_table.sort(key = operator.attrgetter('count'), reverse=True)

for x in range(len(freq_table)):
    sorted_char = ord(sorted_letters[x])
    if freq_table[x].char < sorted_char:
        while True:
            if sorted_char != freq_table[x].char:
                shift_value += 1
                if chr(sorted_char) == 'z':
                    sorted_char = 97
                else:
                    sorted_char += 1
            else:
                break
    else:
        shift_value = sorted_char - freq_table[x].char

    #put shift value into a table












#additional steps goes here(dictionary attacks in case the first attempt fails)
