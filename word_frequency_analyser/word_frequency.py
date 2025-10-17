text = "Data drives decisions. Good data drives great decisions!"

# Clean and split text
text = text.lower().replace(".", "").replace("!", "")
words = text.split()

# Count frequency
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Print alphabetically
for word in sorted(word_count.keys()):
    print(f"{word}: {word_count[word]}")
