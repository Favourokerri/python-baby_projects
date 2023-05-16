def quiz():
    quiz = {
        "question1": { 
            "question": "what is the the capital of nigeria?",
            "answer": "abuja"
        },
        "question2":
        {
            "question": "which continet is nigeria found",
            "answer": "africa"
        },
    }

    score = 0

    for key, value in quiz.items():
        print(value['question'])
        answer = input("Anwers: ")
        if answer == value['answer'].lower():
            score += 1
        print(score)