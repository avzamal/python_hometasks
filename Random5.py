from random import shuffle


def shuffled_text(text):
    list_of_words = text.split(sep=' ')
    for i in range(len(list_of_words)):
        current_word = list_of_words[i]
        current_word_list = [x for x in current_word]
        if len(current_word_list) > 2:
            shuffle_part = current_word_list[1:len(current_word_list)-1]
            shuffle(shuffle_part)
            current_word_list[1:len(current_word_list) - 1] = shuffle_part
        current_word = ''.join(current_word_list)
        list_of_words[i] = current_word
    text = ' '.join(list_of_words)
    return text


print(shuffled_text('Process finished with exit code'))
