import random

responses = [
    "It is certain",
    "Without a doubt",
    "You may rely on it",
    "Yes definitely",
    "It is decidedly so",
    "As I see it, yes",
    "Most likely",
    "Yes",
    "Outlook good",
    "Signs point to yes",
    "Reply hazy try again",
    "Better not tell you now",
    "Ask again later",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "Outlook not so good",
    "My sources say no",
    "Very doubtful",
    "My reply is no"
]

while True:
    question = input("Tell the Magic 8 Ball your question: ").lower()
    
    if "meaning of life" in question:
        print("The Magic 8 Ball says: 42")
    else:
        answer = random.choice(responses)
        print(f"The Magic 8 Ball says: {answer}")

