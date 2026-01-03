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
    print(char_dict)
