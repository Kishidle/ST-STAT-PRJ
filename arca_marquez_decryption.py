import math
import operator
text_cipher = []

def getRelativeFrequency(freq_table, text_cipher):
    rel_freq2 = [0] * 26
    for x in range(len(freq_table)):
        #freq_table[x].req_freq = freq_table.count / len(text_cipher)
        rel_freq2[x] = float(freq_table[x]) / len(text_cipher)
    return rel_freq2
def shiftText2(text, count):
    result = []
    #print count
    for ch in text:
        if ord(ch) != 32:
            temp = ord(ch)
            for x in range(count):

                if chr(temp) == 'a':
                    temp = ord('z')
                else:
                    temp -= 1
            result.append(chr(temp))
        else:
            result.append(chr(32))
    return result
def computeScore(observed_rel, expected_rel):
    score = 0
    for x in range(len(observed_rel)):
        score = score + ((observed_rel[x] - expected_rel[x])**2)/ expected_rel[x]
    return score

#reading text file and putting it to list
file_name = raw_input('File name of the cipher text to be used: ')
with open(file_name) as fileobj:
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
char = freq_table[0].char

shift_value = 0
answer_list = []
for n in range(26):
    if shift_value == 0:
        rel_freq2 = getRelativeFrequency(freq_table2, text_cipher)
        #print rel_freq2
        node = Test_Class(computeScore(rel_freq2, freq_distrib), shift_value)
        answer_list.append(node)
        print "Shift value: " + str(answer_list[n].shift_value) + " and score: " + str(answer_list[n].score)

        shift_value += 1
    else:
        test = shiftText2(text_cipher, shift_value)
        test2 = ''.join(test)
        freq_table2 = [0] * 26
        for ch in test:
            for b in range(len(look_up)):
                if look_up[b] == ord(ch):
                    freq_table2[b] += 1
        rel_freq2 = getRelativeFrequency(freq_table2, text_cipher)
        node = Test_Class(computeScore(rel_freq2, freq_distrib), shift_value)
        answer_list.append(node)
        print "Shift value: " + str(answer_list[n].shift_value) + " and score: " + str(answer_list[n].score)
        shift_value += 1

answer_list.sort(key=operator.attrgetter('score'))

print "\n"
print "Smallest score is " + str(answer_list[0].score) + " found at shift value " + str(answer_list[0].shift_value)
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
