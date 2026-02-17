
sentence = input("Type a sentence: ")
letter = input("Type a letter: ")

lower_sentence = sentence.lower()
counter = 0
for ch in lower_sentence:
    if ch == letter:
        # counter = counter + 1
        counter += 1

t = 'time' if counter==1 else 'times'
print(f"Letter {letter} appears {counter} {t} in sentence.")