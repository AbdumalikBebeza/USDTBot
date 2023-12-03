def remove_char_at(index, input_string):
    if 0 <= index < len(input_string):
        return input_string[:index] + input_string[index + 1:]
    else:
        return "Index out of range"


