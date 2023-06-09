# search list
search_words= ["Python", "C", "OOP", "Hello", "Java"]

# get data from file
with open('input.txt') as word_file:
    words=word_file.read().split('\n')
    for word in search_words:
        # count total matches
        word_count=words.count(word)
        print(f'{word} -> {word_count}')
