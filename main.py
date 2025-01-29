try:
    with open("books/frankenstein.txt", encoding="utf-8") as f:
        file_contents = f.read()
        print("File read successfully!")
except FileNotFoundError:
    print("Could not find the file!")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

def count_characters(text):
    """Counts alphabetic characters in text without using Counter."""
    char_count = {}  # Use a dictionary instead of Counter
    for char in text:
        if char.isalpha():
            char = char.lower()
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

def count_words(text):
    """Counts words in text using regex for better accuracy."""
    import re
    words = re.findall(r'\b\w+\b', text)
    return len(words)

# Count characters and words
print("About to count characters and words...")
char_count = count_characters(file_contents)
word_count = count_words(file_contents)

# Prepare the report
print("\n--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document.\n")

# Sort characters by frequency (highest to lowest)
sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

for char, count in sorted_chars:
    print(f"The '{char}' character was found {count} times")

print("\n--- End report ---")

