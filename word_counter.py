# open text file
text = open("text.txt", "r")

# creating blank dictionary

word_text = {}

# make each word key and count them
for word in text:
    word = word.strip()
    word = word.lower()
    word = word.split(" ")

    for word in word:
        if word in word_text:
            word_text[word] = word_text[word] + 1
        else:
            word_text[word] = 1


# for testing to make sure dictionary works
# print(word_text)

for key in word_text:
    print(key, ":", word_text[key])
