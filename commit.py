

list_of_words = ['hello', 'good bye', 'first', 'last', 'third']
to_print = ''
additional_word = 'welcome'
list_of_words.append(additional_word)

for i in range(len(list_of_words)):
    to_print += list_of_words[i]
    if i != len(list_of_words):
        to_print += ', '

print(to_print)
