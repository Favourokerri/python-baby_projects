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
        print(key)
        print(value['question'])
        answer = input("Anwers: ")
        if answer == value['answer'].lower():
            print("correct")
            score += 1
            print("-------------------------")
        elif answer != value['answer'].lower:
            print("you got this answer wrong, the correct answer is", value['answer'])
            print("--------------------------")
    print("your score total is {} ".format(score))