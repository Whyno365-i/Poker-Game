from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
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

        #TODO Make Cards on UI
        #TODO start on betting system and chips


        self.setWindowTitle('Poker Game')

        self.centralWidget= QWidget()
        self.centralWidget.setStyleSheet('background: #35654D;')
        self.setCentralWidget(self.centralWidget)

        self.main_layout= QVBoxLayout(self.centralWidget)

        self.setMinimumSize(700, 500)

        self.player= []

        self.bot= []

        self.board= []

        self.top_card= 8

        self.button_width= 100
        self.make_cards()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.button_width= self.width()/ 10
        self.button_height= self.height()/ 17

        self.fold.setFixedSize(self.button_width, self.button_height)
        self.call.setFixedSize(self.button_width, self.button_height)
        self.check.setFixedSize(self.button_width, self.button_height)
        self.rise.setFixedSize(self.button_width, self.button_height)

    def make_cards(self):
        self.player_container= QWidget()
        self.player_container.setStyleSheet('background: #FFFFFF;')
        self.player_layout= QHBoxLayout(self.player_container)

        self.button_container= QWidget()
        # self.button_container.setStyleSheet('background: #4dbc29')
        self.button_layout= QGridLayout(self.button_container)



        #Makes every row 1-10 have 100px
        for row in range(3):
            self.button_layout.setRowMinimumHeight(row, 100)

        #Makes every colmun 1-10 have 100px
        for col in range(3):
            self.button_layout.setColumnMinimumWidth(col, 100)

        self.board_container= QWidget()
        self.board_container.setStyleSheet('background: #000000')
        self.board_layout= QGridLayout(self.board_container)

        #Makes every row 1-10 have 100px
        for row in range(6):
            self.board_layout.setRowMinimumHeight(row, 100)

        #Makes every colmun 1-10 have 100px
        for col in range(11):
            self.board_layout.setColumnMinimumWidth(col, 100)

        self.opponent_container= QWidget()
        self.opponent_container.setStyleSheet('background: #000000')
        self.opponent_layout= QGridLayout(self.opponent_container)

        #Makes every row 1-10 have 100px
        for row in range(6):
            self.opponent_layout.setRowMinimumHeight(row, 100)

        #Makes every colmun 1-10 have 100px
        for col in range(11):
            self.opponent_layout.setColumnMinimumWidth(col, 100)




        self.fold= QPushButton('Fold')
        self.fold.setStyleSheet('''
            QPushButton {
                background: #FF0000;
                border: 2px solid #000000;
                border-radius: 3px;
            }

            QPushButton:hover {
                background: #FF3333;
            }
''')

        self.call= QPushButton('Call')
        self.call.setStyleSheet('''
            QPushButton {
                background: #FF0000;
                border: 2px solid #000000;
                border-radius: 3px;
            }

            QPushButton:hover {
                background: #FF3333;
            }
''')

        self.check= QPushButton('Check')
        self.check.setStyleSheet('''
            QPushButton {
                background: #FF0000;
                border: 2px solid #000000;
                border-radius: 3px;
            }

            QPushButton:hover {
                background: #FF3333;
            }
''')

        self.rise= QPushButton('Raise') 
        self.rise.setStyleSheet('''
            QPushButton {
                background: #FF0000;
                border: 2px solid #000000;
                border-radius: 3px;
            }

            QPushButton:hover {
                background: #FF3333;
            }
''')


        self.button_layout.addWidget(self.fold, 2, 1)
        self.button_layout.addWidget(self.call, 3, 1)
        self.button_layout.addWidget(self.check, 2, 2)
        self.button_layout.addWidget(self.rise, 3, 2)

        self.player_layout.addStretch(8)
        self.player_layout.addWidget(self.button_container, alignment= Qt.AlignmentFlag.AlignRight)
        self.player_layout.addStretch(2)

        self.main_layout.addWidget(self.opponent_container)
        self.main_layout.addWidget(self.board_container)
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