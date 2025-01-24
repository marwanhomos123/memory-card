from  PyQt5.QtCore import Qt
from  PyQt5.QtWidgets import (QLabel , QApplication,QWidget, QPushButton, QRadioButton , QRadioButton , QHBoxLayout , QVBoxLayout , QGroupBox)
from random import shuffle, randint

class Questions():
    def __init__(self,question, rightAnswer, wrong1,wrong2,wrong3):
        self.question = question
        self.rightAnswer = rightAnswer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle("Memory Card Application")
question = QLabel("What is the capital of Egypt?")
vlay = QVBoxLayout()
vlay.addWidget(question, alignment= Qt.AlignCenter)


group = QGroupBox("Answer Options:")

rbtn_1 = QRadioButton("Cairo")
rbtn_2 = QRadioButton("Giza")
rbtn_3 = QRadioButton("Alex")
rbtn_4 = QRadioButton("Suez")

hlay = QHBoxLayout()
vlay2 = QVBoxLayout()
vlay3 = QVBoxLayout()


vlay2.addWidget(rbtn_1)
vlay2.addWidget(rbtn_2)

vlay3.addWidget(rbtn_3)
vlay3.addWidget(rbtn_4)

hlay.addLayout(vlay2)
hlay.addLayout(vlay3)

group.setLayout(hlay)
vlay.addWidget(group)





# answer

#deef wa7ed kaman
ansGroup = QGroupBox("Test Result!")
lbl_ans = QLabel("Correct")
hlay2 = QHBoxLayout()
hlay2.addWidget(lbl_ans)
ansGroup.setLayout(hlay2)

vlay.addWidget(ansGroup)
my_win.setLayout(vlay)

btn2 = QPushButton("Answer")
vlay.addWidget(btn2)

my_win.setLayout(vlay)




ansGroup.hide()
# functions to use 
# -------------------------------------------------------------------------------------
def show_result():
    group.hide()
    ansGroup.show()
    btn2.setText("Next Question")


def show_question():
    group.show()
    ansGroup.hide()
    btn2.setText("Answer")
    # group.setExclusive(False)

answers = [rbtn_1, rbtn_2 , rbtn_3 , rbtn_4]
my_win.score = 0
def test():
    if answers[0].isChecked():
        check_answer("correct")
        my_win.score += 1
    else:
        check_answer("incorrect")
    

answers = [rbtn_1, rbtn_2 , rbtn_3 , rbtn_4]
def ask(q: Questions):
    shuffle(answers)
    answers[0].setText(q.rightAnswer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lbl_ans.setText(q.rightAnswer)
    show_question()


def check_answer(res):
    lbl_ans.setText(res)
    show_result()
# -------------------------------------------------------------------------------------
q1 = Questions("What is the capital of Egypt?", "Cairo", "Giza" ,"Alex" , "Suez")   
ask(q1)

questions_list = []
q1 = Questions("Who will win UEFA next year", "barca", "real madrid" ,"ac milan" , "dortmund")
q2 = Questions("What is the best club oat", "real madrid", "barca" ,"man city" , "man united")
q3 = Questions("What is the best game oat", "fortnite", "cod" ,"apex legends" , "valorant")
q4 = Questions("Who will win FNCS next year", "savage" , "clix" , "mongral" , "peter bot")
q5 = Questions("Who is the best at fn oat", "mongral", "savage", "peter bot " , "mero")
q6 = Questions("Who will win the Euros", "Spain", "Italy", "Portugal", "Germany")
q7 = Questions("The GOAT", "Cristiano Ronaldo" , "Messi" , "Lamine Yamal", "Nico Williams")
q8 = Questions("Who has the best celeb" , "Griezmann", "Grimaldo" , "Frimpong" , "Ronaldinho")


questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)
questions_list.append(q4)
questions_list.append(q5)
questions_list.append(q6)
questions_list.append(q7)
questions_list.append(q8)



my_win.total = 1
def next_question():
    print()
    print("total question:",my_win.total)
    print("correct questions: ",my_win.score)
    print("percentage: ", my_win.score/my_win.total*100, "%")
    my_win.total += 1
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def Click_ok():
    if btn2.text() == "Answer":
        test()
    else:
        next_question()

btn2.clicked.connect(Click_ok)
# run the program
# window.resize(400,400)
my_win.show()
app.exec()

# class #class name():
#     def #__init__(self,value):