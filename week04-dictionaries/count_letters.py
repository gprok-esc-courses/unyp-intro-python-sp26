
sentence = input("Type a sentence: ")

sentence_lower = sentence.lower()

letters = {} 

for ch in sentence_lower:
    if ch == ' ':
        continue
    if ch in letters:
        letters[ch] += 1
    else:
        letters[ch] = 1 

# Print the dictionary:
for key in letters:
    print(f"Char {key} appears {letters[key]} times")