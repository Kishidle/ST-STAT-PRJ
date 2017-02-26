import math
import operator
text_cipher = []

def getRelativeFrequency(freq_table, text_cipher):
    rel_freq2 = [0] * 26
    for x in range(len(freq_table)):
        #freq_table[x].req_freq = freq_table.count / len(text_cipher)
        rel_freq2[x] = float(freq_table[x]) / len(text_cipher)
    return rel_freq2
def shiftText(text, count):
    result = []
    #print count
    for ch in text:
        #print "Letter " + ch + " With ASCII value " + str(ord(ch)) + " shifted by value of " + str(count)
        temp = ord(ch) - count
        if temp < 97:
            temp = 97 + (ord(ch) % 26)
        if temp > 122:
            temp = 122 - (ord(ch) % 26)
        result.append(chr(temp))

    #print ''.join(result)
    return result
def shiftText2(text, count):
    result = []
    #print count
    for ch in text:
        temp = ord(ch)
        for x in range(count):

            if chr(temp) == 'a':
                temp = ord('z')
            else:
                temp -= 1
        result.append(chr(temp))
    return result
def computeScore(observed_rel, expected_rel):
    score = 0
    for x in range(len(observed_rel)):
        score = score + ((observed_rel[x] - expected_rel[x])**2)/ expected_rel[x]
    return score

#reading text file and putting it to list
with open("textcipher2.txt") as fileobj:
    for line in fileobj:
        for ch in line:
            text_cipher.append(ch) #we can replace this so that it already counts the frequency of the letter maybe?

class Char_Class:
    def __init__(self, char, count, rel_freq):
        self.char = char
        self.count = count
        self.rel_freq = rel_freq

class Test_Class:
    def __init__(self, score, shift_value):
        self.score = score
        self.shift_value = shift_value

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
freq_table2 = [0] * 26

#use chr(num) to change 97 into a
for x in range(26):
    look_up.append(a)
    char_test = Char_Class(a, 0, 0)
    freq_table[x] = char_test
    a += 1

#finds the frequency count of each letter in the text_cipher
for ch in text_cipher:
    for x in range(len(look_up)):
        if look_up[x] == ord(ch):
            freq_table[x].count += 1
            freq_table2[x] += 1

print ("What method would you like to use? [1] Bruteforce Method [2] Less BruteForce Method")
#ask for input

#bruteforce method?: find the largest value of freq_table, which is the most frequent character. find its index and then compare with freq_distrib

freq_table.sort(key = operator.attrgetter('count'), reverse=True) #this finds the largest value in the list and its index

#print "count: " + str(freq_table[0].count)

char = freq_table[0].char

for x in range(26):
    sorted_char = ord(sorted_letters[x])
    shift_value = 0
    while True:
        if sorted_char != char:
            shift_value += 1
            if chr(sorted_char) == 'z':
                sorted_char = 97
            else:
                sorted_char += 1
        else:
            break
    #shift the text!
    shiftText(text_cipher, shift_value)

#shift to e going left, do this until you exhaust every letter in the freq_table. this is one option

#less bruteforce method: comparing most common in text to most common in table, 2nd most common in text to 2nd most common in table, and so on...

#algorithm 2

#getting the relative frequency



shift_table = []
shift_value = 0
answer_list = []
for n in range(26):
    if shift_value == 0:
        rel_freq2 = getRelativeFrequency(freq_table2, text_cipher)
        #print rel_freq2
        node = Test_Class(computeScore(rel_freq2, freq_distrib), shift_value)
        answer_list.append(node)
        print "Shift value: " + str(answer_list[n].shift_value) + " and score: " + str(answer_list[n].score)
        print "\n"
        shift_value += 1
    else:
        test = shiftText2(text_cipher, shift_value)
        test2 = ''.join(test)
        freq_table2 = [0] * 26
        #print test
        #print "\n"
        for ch in test:
            for b in range(len(look_up)):
                if look_up[b] == ord(ch):
                    freq_table2[b] += 1
        #print test
        #print freq_table2
        rel_freq2 = getRelativeFrequency(freq_table2, text_cipher)
        #print rel_freq2
        node = Test_Class(computeScore(rel_freq2, freq_distrib), shift_value)
        answer_list.append(node)
        print "Shift value: " + str(answer_list[n].shift_value) + " and score: " + str(answer_list[n].score)
        print "\n"
        shift_value += 1
answer_list.sort(key=operator.attrgetter('score'))
#print answer_list[0].shift_value

print "\n"
print "Cipher text: " + ''.join(text_cipher)
print "\n"
print "Shift to the left " + str(answer_list[0].shift_value) + " times"
print "\n"
test = shiftText2(text_cipher, answer_list[0].shift_value)
test2 = ''.join(test)
print "Original text: " + test2





    #put shift value into a table












#additional steps goes here(dictionary attacks in case the first attempt fails)
