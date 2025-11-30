import sys


def get_num_words(text):
    words = text.split()
    return (len(words))

def get_word_count(text):
    l_text = text.lower()
    letter_dict = {}
    for n in l_text:
        if n in letter_dict:
            letter_dict[n] += 1
        else:
            letter_dict[n] = 1
    return letter_dict

def sort_on(d):
    return d["num"]

def chars_list_to_sorted_list(nums_chars_dict):
    sorted_list = []
    for ch in nums_chars_dict:
        sorted_list.append({"char": ch, "num": nums_chars_dict[ch]})
    sorted_list.sort(reverse = True, key = sort_on)
    return sorted_list
