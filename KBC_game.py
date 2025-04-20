questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Who is known as the father of computers?",
        "options": ["A. Alan Turing", "B. Charles Babbage", "C. Elon Musk", "D. Bill Gates"],
        "answer": "B"
    },
    {
        "question": "Which language is used to write AI programs?",
        "options": ["A. Python", "B. C++", "C. Java", "D. HTML"],
        "answer": "A"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    user = input("Your answer (A/B/C/D): ").strip().upper()
    if user == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is", q["answer"])

print(f"\nYou scored {score} out of {len(questions)}!")
