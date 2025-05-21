import csv

def ask_question(question, options, correct_answer):
    print(question)
    for option in options:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer was {correct_answer}.\n")
        return False

def load_questions_from_csv(filename):
    questions = []
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                questions.append({
                    "question": row["question"],
                    "options": [f"A) {row['A']}", f"B) {row['B']}", f"C) {row['C']}", f"D) {row['D']}"],
                    "correct": row["answer"].upper()
                })
    except FileNotFoundError:
        print("CSV file not found. Using default questions.\n")
    return questions

def main():
    print("Welcome to the Python Quiz Game!")
    name = input("What's your name? ")
    print(f"Hello, {name}! Let's start the quiz.\n")

    questions = load_questions_from_csv("questions.csv")
    if not questions:
        # Default questions if CSV not found
        questions = [
            {
                "question": "What is the output of print(2**3)?",
                "options": ["A) 6", "B) 8", "C) 9", "D) 5"],
                "correct": "B"
            },
            {
                "question": "Which of the following is used to define a function in Python?",
                "options": ["A) func", "B) def", "C) define", "D) function"],
                "correct": "B"
            },
            {
                "question": "What is the correct file extension for Python files?",
                "options": ["A) .pt", "B) .pyt", "C) .py", "D) .pyth"],
                "correct": "C"
            },
            {
                "question": "What is 5 // 2?",
                "options": ["A) 2.5", "B) 2", "C) 3", "D) 5"],
                "correct": "B"
            },
            {
                "question": "What type is 3.14?",
                "options": ["A) int", "B) float", "C) string", "D) bool"],
                "correct": "B"
            }
        ]

    score = 0
    for idx, q in enumerate(questions[:5], 1):
        print(f"Question {idx}:")
        if ask_question(q["question"], q["options"], q["correct"]):
            score += 1

    print(f"{name}, your final score is {score} out of 5.")

if __name__ == "__main__":
    main()