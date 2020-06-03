import collections
class MostFrequentWord:
    def getMostFrequentWord(self, word_list):
        frequency_dict = collections.Counter()
        for word in word_list:
            frequency_dict[word] += 1
        print frequency_dict

if __name__ == '__main__':
    most_frequent_word = MostFrequentWord()
    most_frequent_word.getMostFrequentWord(["aa", "bb", "aa"])