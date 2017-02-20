import math

text_cipher = []

#reading text file and putting it to list
with open("textcipher.text") as fileobj:
    for line in fileobj:
        for ch in line:
            text_cipher.append(ch)

#initialization of frequency distribution of letters
#make a list for the frequency distribution, then make a look-up list for the letters?
freq_distrib = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024,
                0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.024, 0.002, 0.020, 0.001]


look_up = [None] * 27

a = 97
for x in range(27):
    look_up.append(a)
    a += 1


#algorithm for frequency analysis goes here








#additional steps goes here(dictionary attacks in case the first attempt fails)
