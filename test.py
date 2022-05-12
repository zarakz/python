def make_reverse_each_word(my_string):
    split_string = my_string.split()
    for i in range(0, len(split_string)):
        split_string[i] = split_string[i][::-1]
    new_reversed_string = ''
    for i in range(0, len(split_string)):
        new_reversed_string += split_string[i] + " "
    new_reversed_string = new_reversed_string.strip()
    return new_reversed_string


input_string = input("Enter a sentence: ")
print(make_reverse_each_word(input_string))
