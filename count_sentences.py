def count_words(input_string):
    words = input_string.split()
    return len(words)

input_string = "This is a sample input string"
word_count = count_words(input_string)
print("Number of words in input string:", word_count)
