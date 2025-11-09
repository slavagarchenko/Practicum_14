def count_leaky_letters(sentence: str) -> int:
    """
    Finds leaky letters in the sentence and returns its amount

    Args:
        sentence (str): analyzed sentence for finding leaky letters

    Returns:
        count (int): the amount of leaky letters in the sentence
    """
    leaky_letters = ["a", "b", "d", "e", "g", "o", "p", "q"]
    count = 0

    for item in sentence:
        if item in leaky_letters:
            count += 1

    return count


sentence = input("Введите предложение: ")
letters_sentence = sentence.replace(" ", "")
count = count_leaky_letters(sentence)

print(f"Количество букв с отверстиями: {count},"
      f"количество букв без отверстий: {len(letters_sentence) - count}")

leaky_words = []
for word in sentence.split():
    if count_leaky_letters(word) > 1:
        leaky_words.append(word)

print(leaky_words)
