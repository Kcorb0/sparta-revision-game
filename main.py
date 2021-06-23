# Shows user a question
# User provides an answer as an input of what they think the answer should be
# Shows user the prefered answer
from topics import agile, data_consepts, database_design, sql, python


def get_question():
    return agile[1]


run = True
qcnt = 1
end_answer = True

while run:

    question = get_question()[0]
    answer = get_question()[1]

    print(f"\nQuestion {qcnt}: {question}\n")

    while end_answer:
        user_answer = input(" - ")
        if user_answer == "":
            end_answer = False

    print(f"\n{answer}")

    qcnt += 1
    break
