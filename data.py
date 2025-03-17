import requests

# Fetch trivia questions from API
parameters = {
    "amount": 20,
    "category": 11,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

# Extract question data
question_data = response.json()["results"]
# print(question_data)



