def list_and_string(sentence: str) -> None:
    """
    The function takes a string, converts it to a list of characters,
    sorts the list and converst it back to a string

    Args:
        sentence (str): The initial conversation for converting

    Returns:
        None
    """
    symbols_sentence = sentence.replace(" ", "")
    symbols = [item for item in symbols_sentence]
    symbols.sort()
    new_string = "".join(symbols)
    print(new_string)


sentence = input("Введите предложение: ")
list_and_string(sentence)
