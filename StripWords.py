file = open('guess_words.txt','r')

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
'o','p','q','r','s','t','u','v','w','x','y','z']

words = []
grabbed_word = ''

for line in file:
    for char in line:
        if char.lower() in alpha:
            grabbed_word += char.lower()
        else:
            if grabbed_word:
                words.append(grabbed_word)
                grabbed_word = ''

print(words)
file.close()
new_file = open('top_words.txt','a+')
for word in words:
    new_file.write(word + '\n')
    