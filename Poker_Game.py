from PySide6.QtWidgets import QApplication, QMainWindow, QWidget


def main():
    app= QApplication()
    window= Poker()
    window.showMaximized()
    app.exec()


class Poker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Poker Game')

        self.setMinimumSize(700, 500)

        self.setStyleSheet('background: #35654D;')

        self.make_cards()

    def make_cards(self):
        card_num= {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

        card_suit= ['Hearts', 'Diamonds', 'Clubs', 'Spades']

        self.cards= []

        suit_x= 0 

        for _event in range(4):
            for i in range(len(card_num)):
                self.cards.append((list(card_num)[i], card_suit[suit_x]))

                if list(card_num)[i] == 'Ace':
                    suit_x+=1




if __name__ == '__main__':
    main()
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QHBoxLayout
import random


def main():
    app= QApplication()
    window= Poker()
    #TODO change show to showMaxinmum
    window.show()
    app.exec()


class Poker(QMainWindow):
    def __init__(self):
        super().__init__()

        #TODO make the different layouts
        #TODO fix the buttons
        #TODO start on betting system and chips


        self.setWindowTitle('Poker Game')

        self.setStyleSheet('background: #35654D;')
        self.setCentralWidget(self)

        self.main_layout= QHBoxLayout(self)

        self.setMinimumSize(700, 500)

        self.player= []

        self.bot= []

        self.board= []

        self.top_card= 8


        self.make_cards()

    def make_cards(self):
        self.player_container= QWidget()
        self.player_container.setStyleSheet('background: #clear;')
        self.player_layout= QGridLayout(self.player_container)

        #Makes every row 1-10 have 50px
        for row in range(11):
            self.player_layout.setRowMinimumHeight(row, 100)

        #Makes every colmun 1-10 have 50px
        for col in range(11):
            self.player_layout.setColumnMinimumWidth(col, 100)


        self.fold= QPushButton('Fold')
        self.fold.setFixedWidth(100)
        self.fold.setStyleSheet('''
            QPushButton {
                background: #FF0000;
                border: 2px solid #000000;
                border-radius: 3px;
                padding-top: 10px;
                padding-bottom: 10px;
            }

            QPushButton:hover {
                background: #FF3333;
            }
''')

        self.call= QPushButton('Call')
        self.call.setFixedWidth(100)
        self.call.setStyleSheet('''
            QPushButton {
                background: #FF0000;
                border: 2px solid #000000;
                border-radius: 3px;
                padding-top: 10px;
                padding-bottom: 10px;
            }

            QPushButton:hover {
                background: #FF3333;
            }
''')

        self.check= QPushButton('Check')
        self.check.setFixedWidth(100)
        self.check.setStyleSheet('''
            QPushButton {
                background: #FF0000;
                border: 2px solid #000000;
                border-radius: 3px;
                padding-top: 10px;
                padding-bottom: 10px;
            }

            QPushButton:hover {
                background: #FF3333;
            }
''')

        self.rise= QPushButton('Raise') 
        self.rise.setFixedWidth(100)
        self.rise.setStyleSheet('''
            QPushButton {
                background: #FF0000;
                border: 2px solid #000000;
                border-radius: 3px;
                padding-top: 10px;
                padding-bottom: 10px;
            }

            QPushButton:hover {
                background: #FF3333;
            }
''')


        self.player_layout.addWidget(self.fold, 9, 7)

        self.player_layout.addWidget(self.call, 10, 7)

        self.player_layout.addWidget(self.check, 9, 8)

        self.player_layout.addWidget(self.rise, 10, 8)        

        self.player_layout.setColumnStretch(6, 5)
        self.player_layout.setColumnStretch(9, 5)

        self.player_layout.setRowStretch(8, 10)
        self.player_layout.setRowStretch(9, 10)
        self.player_layout.setRowStretch(10, 1)

        self.main_layout.addWidget(self.player_container)


        card_num= {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

        card_suit= ['Hearts', 'Diamonds', 'Clubs', 'Spades']

        self.order_cards= []

        suit_x= 0 

        for _event in range(4):
            for i in range(len(card_num)):
                self.order_cards.append((list(card_num)[i], card_suit[suit_x]))

                if list(card_num)[i] == 'Ace':
                    suit_x+=1

        self.cards= random.sample(self.order_cards, len(self.order_cards))

        self.pass_out()

    def pass_out(self):
        self.player.append(self.cards[1])
        self.player.append(self.cards[3])

        self.bot.append(self.cards[2])
        self.bot.append(self.cards[4])

        #There will be a step to bet

    def board_pass_out(self):
        self.board.append(self.cards[5], self.cards[6], self.cards[7])




if __name__ == '__main__':
    main()