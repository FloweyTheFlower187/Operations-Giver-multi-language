import random
from termcolor import colored, cprint

def question_refaire():
    texte_question = colored("Deseja repetir a operação? (Y/n)", color="light_yellow", attrs=["bold","italic"])
    question = input(texte_question).lower()
    if question == "y":
        refaire()
    if question == "n":
        cprint("Até nos encontrarmos novamente", color="blue", attrs=["bold","italic"])


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

    texte_InputJoueur = colored("Qual é o resultad? ?", color="magenta",attrs=["bold","italic"])
    InputJoueur = int(input(texte_InputJoueur))

    if InputJoueur == result:
        cprint("Bom trabalho ! :)",color="green" , attrs=["italic","bold"])
        question_refaire()
    else:
        cprint(f"Está enganado! O resultado foi : {result}",color="red" , attrs=["italic","bold"])
        question_refaire()

refaire()