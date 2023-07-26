#-----------------------
def newgame():
    guesses = []
    correct_guesses = 0
    questions_num = 1
    for i in questions:
        print("------------------")
        print(i)
        for j in options[questions_num-1]:
            print(j)
        questions_num += 1
        quess = input("Enter Your guesses : [A,B,C,D] ? ")
        quess = quess.upper()
        guesses.append(quess)
        correct_guesses += checkanswer(questions.get(i), quess)
    displayscore(correct_guesses,guesses)


#-----------------------
def checkanswer(rightans, currentguess):
    if rightans == currentguess:
        return 1
    else:
        return 0


#-----------------------
def displayscore(correntguess,guesses):
    print("-----------------")
    print("Correct Guesses : ", end='')
    for i in questions.values():
        print(i, end=' ')
    print()
    print("-----------------")
    print("Your Guesses    : ", end='')
    for i in guesses:
        print(i, end=' ')
    print()
    print("-----------------")
    value = (correntguess/len(questions))*100
    print("Your score is : "+str(value)+"%")


#-----------------------
def playagain():
    print()
    now = input("You want to play again ? Yes / No : ")
    now = now.upper()
    if now == "YES":
        return True
    else:
        return False


questions = {
    "1. Who developed Python Programming Language?": "C",
    "2. Which type of Programming does Python support?": "D",
    "3. Is Python case sensitive when dealing with identifiers?": "B",
    "4. Which of the following is the correct extension of the Python file?": "C",
    "5. Is Python code compiled or interpreted?": "A"
}
options = [
    ["a) Wick van Rossum", "b) Rasmus Lerdorf", "c) Guido van Rossum", "d) Niene Stom"],
    ["a) object-oriented programming", "b) structured programming", "c) functional programming", "d) all of the mentioned"],
    ["a) no", "b) yes", "c) machine dependent", "d) none of the mentioned"],
    ["a) .python", "b) .pl", "c) .py", "d) .p"],
    ["a) Python code is both compiled and interpreted", "b) Python code is neither compiled nor interpreted", "c) Python code is only compiled", "d) Python code is only interpreted"]
]
newgame()
while playagain():
    newgame()
print()
print("Thank you for playing game")
