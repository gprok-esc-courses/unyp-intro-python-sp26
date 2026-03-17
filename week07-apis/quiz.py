import requests 
import html 

response = requests.get("https://opentdb.com/api.php?amount=5&type=boolean")

response_data = response.json()
data = response_data['results'] 

score = 0

for row in data:
    print(html.unescape(row['question']))
    answer = input("Give answer (T/F): ")
    answer = answer.upper()
    if row['correct_answer'] == "True" and answer == 'T':
        score += 1
    elif row['correct_answer'] == "False" and answer == 'F':
        score += 1

print("Quiz Completed")
print(f"Score: {score}/5")


