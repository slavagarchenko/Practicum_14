sentence = input("Введите предложение: ")
words = []

for word in sentence.split():
    cleaned_word = word.strip('.,!?;:()\"\'')
    words.append(cleaned_word)

print(words)
