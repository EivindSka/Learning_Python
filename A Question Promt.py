from question import Question    #importerer class(Question) fr question.py

question_prompt = [
    "What colour is the ocean? \n (a) Yellow\n (b) Blue \n (c) Green\n\n ",
    "What month is it? \n (a) October\n (b) September\n (c) November\n\n ",
    "Who is Darth Vader? \n (a) Anakin Skywalker \n (b) Yoda \n (c) Obi Wan \n\n",
    "What is thee best stock? \n (a) Gamestop \n (b) Tesla \n (c) Amazon \n\n"
    ]


questions = [
    Question(question_prompt[0], "b"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "a"),
    Question(question_prompt[3], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.promt)
        if answer == question.answer:
            score += 1
    print ("You got " + str(score) + "/" + str(len(questions)) + " Correct")

run_test(questions)
