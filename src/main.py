from models.frequent_word_finder import FrequentWordFinder


words = ["love", "peace", "joy", "love", "happiness", "love", "joy"]

finder = FrequentWordFinder(words)

finder.find_the_most_frequent_word()

result = f"""
The most frequent word is {finder.most_frequent}
with {finder.word_count[finder.most_frequent]} occurrences."""

print(result)
