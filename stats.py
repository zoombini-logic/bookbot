def word_count(fulltext):
    wordarray = fulltext.split()
    return len(wordarray)

def count_chars(fulltext):
    char_dict = {}
    for c in fulltext:
        lowerc = c.lower()
        if (lowerc in char_dict):
            char_dict[lowerc] += 1
        else: 
            char_dict[lowerc] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def char_sort(inc_dict):
    dict_list = []
    single_dict = {}
    for char_key in inc_dict: 
        single_dict = {}
        single_dict["char"] = char_key
        single_dict["num"] = inc_dict[char_key]
        dict_list.append(single_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return (dict_list)

