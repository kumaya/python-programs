# Find all anagrams of a word in a file.
# Input -  only file name and word.
# Output - all set of word in file that are anagrams of word.

import pickle
import time
import os

# pre processing of anagrams in a file to serialized object
def anagram_formulater(filename, sObj):
    dict_of_anagrams = {}
    with open(filename, 'r') as f:
        for lines in f.readlines():
            words = lines.split()
            for word in words:
                tmp_word = ''.join(sorted(word))
                if tmp_word not in dict_of_anagrams.keys():
                    dict_of_anagrams[tmp_word] = [word]
                else:
                    dict_of_anagrams[tmp_word].append(word)
    final_dict = {}
    for key, val in dict_of_anagrams.iteritems():
        final_dict[key] = set(val)

    serializedObj = open(sObj, 'ab')
    pickle.dump(final_dict, serializedObj)
    serializedObj.close()
    return


def anagram_grabber(word, serialized_db):
    s = open(serialized_db, 'rb')
    s1 = pickle.load(s)
    sorted_word = ''.join(sorted(word))
    s.close()
    if sorted_word in s1.keys():
        return list(s1[sorted_word])


if __name__ == '__main__':
    """
    Anyakm amanky nala akmany akmyna amyank
    alan laan rara mayakk knayma
    """
    filename = "./anagramsFromFile.py"
    serialized_db = "/tmp/serializedObj.db"
    word = "akmany"

    start = time.time()
    if not os.path.exists(serialized_db):
        anagram_formulater(filename, serialized_db)

    print anagram_grabber(word, serialized_db)
    end = time.time()
    print end - start
