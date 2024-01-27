import random

def ask_question(question, options, correct_answer):
    """
    Ask a multiple-choice question and get the user's answer.

    Args:
        question (str): The question to be asked.
        options (list): List of multiple-choice options.
        correct_answer (str): The correct answer to the question.

    Returns:
        int: 1 if the user's answer is correct, 0 otherwise.
    """
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    user_answer = input("Enter the number corresponding to your answer: ")
    if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
        user_answer_index = int(user_answer) - 1
        if options[user_answer_index] == correct_answer:
            print("Correct!\n")
            return 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}\n")
            return 0
    else:
        print("Invalid input. Please enter a valid option.\n")
        return 0

# Predicting the final score
def run_quiz(questions):
    """
    Run the quiz with a list of questions.

    Args:
        questions (list): List of dictionaries containing questions, options, and correct answers.
    """
    total_score = 0
    random.shuffle(questions)

    for question in questions:
        total_score += ask_question(**question)

    print(f"Your final score is: {total_score}/{len(questions)}")

# Question for the quiz
    
if __name__ == "__main__":
    quiz_questions = [
        {
            "question": "What is the capital of India?",
            "options": ["Paris", "Delhi", "Rome", "Portugal"],
            "correct_answer": "Delhi",
        },
        {
            "question": "Which programming language is this quiz written in?",
            "options": ["Java", "Python", "C++", "JavaScript"],
            "correct_answer": "Python",
        },
        {
            "question": "What is the result of 5 + 5?",
            "options": ["7", "8", "9", "10"],
            "correct_answer": "10",
        },
        {
            "question": "How many days are there in January?",
            "options": ["30", "28", "29", "31"],
            "correct_answer": "31",
        },
        # Add more questions as needed
    ]

    run_quiz(quiz_questions)
