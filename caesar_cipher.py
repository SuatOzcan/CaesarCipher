import string

alphabet = list(string.ascii_lowercase)
#alphabet.append(string.punctuation)

alphabet.append(' ')

# punctuations = ['.',',',':',':','!']
# for punctuation in punctuations:
#     alphabet.append(punctuation)

for punctuation in string.punctuation:
    alphabet.append(punctuation)


key = 3
text = 'zebras are white.'
cipher_text = []

print(text)
for letter in text:
    index = alphabet.index(letter)
    index = (index+key) % (len(alphabet))
    cipher_letter = alphabet[index]
    cipher_text.append(cipher_letter)
cipher_text = ''.join(cipher_text)
print(cipher_text)

text = []

for letter in cipher_text:
    index = alphabet.index(letter)
    if index - key >= 0:
        index = alphabet.index(letter)
        index -= key
        clean_letter = alphabet[index]
        text.append(clean_letter)
    else:
        index = (len(alphabet)) - (key - index) 
        clean_letter = alphabet[index]
        text.append(clean_letter)

text = ''.join(text)
print(text)