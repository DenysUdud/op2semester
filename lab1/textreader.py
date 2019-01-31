def input_data(path):
    """
    str -> list

    Returns the list of characters from the file.
    """
    list_lines = []
    with open(path, "r", encoding="UTF-8") as file:
        line = file.readline()
        while len(line) > 0:
            list_lines.append(line.strip("\n "))
            line = file.readline()
    return list_lines


def row_extend(row):
    """
    list -> list

    Returns the extended row with sorted vowels by their frequency in the row.
    """
    dict_letters = {}
    set_godd_letters = (A, E, I, O, U, Y)
    for word in row:
        for letter in row:
            letter = letter.upper()
            if letter in set_godd_letters:
                if letter in dict_letters.keys():
                    dict_letters[letter] = dict_letters[letter] + 1
                else:
                    dict_letters[letter] = 1

    pass


def column_extend(column):
    """
    list -> list

    Returns the extended column with sorted consonants without duplication.
    """
    for row in column:
        row_extend(row.split())
    pass


def characters_info(in_path, out_path):
    """
    str, str -> None

    The main function that reads the data from the file, processes it and
    outputs to the other file.
    """
    list_rows = input_data(in_path)
    column_extend(list_rows)


print(input_data("text_1.txt"))
