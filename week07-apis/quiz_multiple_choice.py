import requests 
import html 
import random

response = requests.get("https://opentdb.com/api.php?amount=5&type=multiple")

response_data = response.json()
data = response_data['results'] 

score = 0

for row in data:
    print(html.unescape(row['question']))
    correct = html.unescape(row['correct_answer'])
    all_answers = row['incorrect_answers']
    all_answers.append(row['correct_answer'])
    random.shuffle(all_answers)
    for i in range(4):
        all_answers[i] = html.unescape(all_answers[i])
        print(f"{i+1}. {all_answers[i]}")
    choice = int(input("Choose correct answer 1 .. 4: "))
    if choice > 0 and choice < 5:
        user_answer = all_answers[choice - 1]
        if user_answer == correct:
            score += 1

    

print("Quiz Completed")
print(f"Score: {score}/5")