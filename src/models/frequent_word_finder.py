class FrequentWordFinder:
    def __init__(self, wordlist):
        self._wordlist = wordlist
        self._word_count = {}
        self._most_frequent = ""

    @property
    def most_frequent(self):
        return self._most_frequent

    @property
    def word_count(self):
        return self._word_count

    def _count_ocurrences(self):
        print(self._wordlist)
        for word in self._wordlist:
            self._word_count[word] = self._word_count.get(word, 0) + 1

    def find_the_most_frequent_word(self):
        self._count_ocurrences()
        self._most_frequent = max(self._word_count, key=self._word_count.get)
