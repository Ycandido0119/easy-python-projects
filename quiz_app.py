import json
import os
import random
import re
from datetime import datetime

QUESTIONS_FILE = "questions.json"

DEFAULT_QUESTIONS = {
  "easy": [
    {"question": "What is the capital of Italy?", "answers": ["Rome"]},
    {"question": "What is the colour scheme of the Kenyan Flag?", "answers": ["Black, Red, Green and White", "black red green white"]},
    {"question": "What is the largest mammal in the world?", "answers": ["Blue Whale", "Blue whale"]},
    {"question": "What is the smallest prime number?", "answers": ["2", "two"]},
    {"question": "What planet is known as the Red Planet?", "answers": ["Mars", "mars"]}
  ],
  "medium": [
    {"question": "What is the hardest natural substance on Earth?", "answers": ["Diamond", "diamond"]},
    {"question": "Which mountain in Kenya is also the highest point in Africa?", "answers": ["Mount Kenya", "Mount kenya", "mount kenya"]},
    {"question": "What is the largest desert in the world?", "answers": ["Sahara Desert", "Sahara"]},
    {"question": "What is the longest river in the world?", "answers": ["Nile River", "Nile"]},
    {"question": "What is the largest ocean on Earth?", "answers": ["Pacific Ocean", "Pacific"]}
  ],
  "hard": [
    {"question": "What is the smallest country in the world?", "answers": ["Vatican City", "Vatican"]},
    {"question": "What is the rarest blood type in the world?", "answers": ["AB Negative", "AB-"]},
    {"question": "What is the most spoken language in the world?", "answers": ["Mandarin Chinese", "Mandarin"]},
    {"question": "What is the largest island in the world?", "answers": ["Greenland"]},
    {"question": "What is the deepest point in the world's oceans?", "answers": ["Mariana Trench", "Mariana Trench"]}
  ]
}

def normalize(text: str) -> str:
    text = text or ""
    text = text.lower().strip()
    # keep letters, numbers and spaces
    return re.sub(r"[^a-z0-9 ]", "", text)

def load_questions() -> dict:
    if os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    # file missing, write defaults
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(DEFAULT_QUESTIONS, f, ensure_ascii=False, indent=2)
    return json.loads(json.dumps(DEFAULT_QUESTIONS))  # deep copy

def save_questions(qs: dict) -> None:
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

def ask_question(qobj: dict) -> bool:
    prompt = qobj["question"] + "\nYour answer: "
    user = input(prompt).strip()
    if normalize(user) in [normalize(a) for a in qobj.get("answers", [])]:
        print("Correct!")
        return True
    print("Wrong. Correct answer(s): " + ", ".join(qobj.get("answers", [])))
    return False

def start_quiz(level: str, questions: dict) -> None:
    level = level.lower()
    pool = questions.get(level, [])
    if not pool:
        print(f"No questions found for level: {level}")
        return
    qlist = pool[:]
    random.shuffle(qlist)
    score = 0
    wrong_list = []
    for q in qlist:
        ok = ask_question(q)
        if ok:
            score += 1
        else:
            wrong_list.append(q)
    total = len(qlist)
    accuracy = round((score / total) * 100, 1) if total else 0
    print(f"\nResult: {score} out of {total}")
    print(f"Wrong: {len(wrong_list)}")
    print(f"Accuracy: {accuracy}%")
    if wrong_list:
        print("\nReview wrong answers:")
        for q in wrong_list:
            print(f"- {q['question']} -> {', '.join(q['answers'])}")

def add_question(questions: dict) -> None:
    level = input("Choose difficulty (easy/medium/hard): ").strip().lower()
    if level not in ["easy", "medium", "hard"]:
        print("Invalid difficulty. Return to menu.")
        return
    qtext = input("Enter question text: ").strip()
    answers_raw = input("Enter acceptable answers separated by | : ").strip()
    answers = [a.strip() for a in answers_raw.split("|") if a.strip()]
    if not qtext or not answers:
        print("Question or answers missing. Return to menu.")
        return
    questions.setdefault(level, []).append({"question": qtext, "answers": answers})
    save_questions(questions)
    print("Question saved.")

def main() -> None:
    questions = load_questions()
    while True:
        print("\nQuiz Menu")
        print("1 Play quiz")
        print("2 Add question")
        print("3 Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            level = input("Choose difficulty (easy/medium/hard): ").strip().lower()
            start_quiz(level, questions)
        elif choice == "2":
            add_question(questions)
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
