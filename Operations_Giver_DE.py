import random
from termcolor import colored, cprint

def question_refaire():
    texte_question = colored("Möchten Sie eine Operation wiederholen? ? (Y/n)", color="light_yellow", attrs=["bold","italic"])
    question = input(texte_question).lower()
    if question == "y":
        refaire()
    if question == "n":
        cprint("Auf Wiedersehen", color="blue", attrs=["bold","italic"])


def refaire():

    global operation , x , y , result , InputJoueur

    x = random.randint(1, 100)
    y = random.randint(1, 100)

    operation = random.randint(1, 4)

    if operation == 1 :
        operation = "+"
        result = (x + y)
    if operation == 2 :
        operation = "-"
        result = (x - y)
    if operation == 3 :
        operation = "/"
        result = (x // y)
    if operation == 4 :
        operation = "*"
        result = (x * y)


    cprint(f"{x} {operation} {y}", "blue" , attrs=["bold","italic"])

    texte_InputJoueur = colored("Was ist das Ergebnis? ?", color="magenta",attrs=["bold","italic"])
    InputJoueur = int(input(texte_InputJoueur))

    if InputJoueur == result:
        cprint("Gut gemacht ! :)",color="green" , attrs=["italic","bold"])
        question_refaire()
    else:
        cprint(f"Du irrst dich! Das Ergebnis war : {result}",color="red" , attrs=["italic","bold"])
        question_refaire()

refaire()