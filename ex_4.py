sentence = input("Введите предложение: ")
words = []

for word in sentence.split():
    cleaned_word = word.strip('.,!?;:()\"\'')
    if cleaned_word not in words:
        words.append(cleaned_word)

words = [word for word in words if word]
print(words)
