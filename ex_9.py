text = ""
while True:
    line = input()
    if line == "":
        break
    text = text + line + " "
text = text.lower()

words = []
for word in text.split():
    cleaned_word = word.strip('.,!?;:()\"\'')
    if cleaned_word:
        words.append(cleaned_word)

word_order = []
word_count = {}

for word in words:
    if word not in word_count:
        word_count[word] = 0
        word_order.append(word)
    word_count[word] += 1

sorted_words = sorted(
    word_order,
    key=lambda word: (
        -word_count[word],
        word_order.index(word)
    )
)

for word in sorted_words:
    print(word)
