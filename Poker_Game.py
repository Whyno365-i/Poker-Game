from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Qt, QTimer
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

        self.dealer= True

        self.win= False

        self.three_button= False

        self.two_button= False

        self.make_cards()

    def resizeEvent(self, event):
        super().resizeEvent(event)

        if self.three_button== True:
            self.button_width= self.width()// 10
            self.button_height= self.height()// 17

            self.fold.setFixedSize(self.button_width * 2, self.button_height)
            self.call.setFixedSize(self.button_width, self.button_height)
            self.check.setFixedSize(self.button_width, self.button_height)
            self.rise.setFixedSize(self.button_width, self.button_height)

        elif self.two_button== True:
            self.button_width= self.width()// 10
            self.button_height= self.height()// 17

            self.fold.setFixedSize(self.button_width, self.button_height)
            self.call.setFixedSize(self.button_width, self.button_height)
            self.check.setFixedSize(self.button_width * 2, self.button_height)
            self.rise.setFixedSize(self.button_width * 2, self.button_height)

        else:
            self.button_width= self.width()// 10
            self.button_height= self.height()// 17

            self.fold.setFixedSize(self.button_width, self.button_height)
            self.call.setFixedSize(self.button_width, self.button_height)
            self.check.setFixedSize(self.button_width, self.button_height)
            self.rise.setFixedSize(self.button_width, self.button_height)

        QTimer.singleShot(0, self.update_card_sizes)

    def update_card_sizes(self):
        backup_height= int(self.height() * .22)

        backup_width= int(backup_height / 1.43)


        self.card_1.setFixedSize(backup_width, backup_height)             
        self.card_2.setFixedSize(backup_width, backup_height)    




    def make_cards(self):
        self.player_container= QWidget()
        self.player_container.setStyleSheet('background: #FFFFFF;')
        self.player_layout= QHBoxLayout(self.player_container)

        self.button_container= QWidget()
        self.button_layout= QGridLayout(self.button_container)
        self.button_layout.setVerticalSpacing(1)
        self.button_layout.setHorizontalSpacing(1)

        self.board_container= QWidget()
        self.board_container.setStyleSheet('background: #000000')
        self.board_layout= QGridLayout(self.board_container)

        #Makes every row 1-5 have 100px
        for row in range(6):
            self.board_layout.setRowMinimumHeight(row, 100)

        #Makes every colmun 1-10 have 100px
        for col in range(11):
            self.board_layout.setColumnMinimumWidth(col, 100)

        self.opponent_container= QWidget()
        self.opponent_container.setStyleSheet('background: #000000')
        self.opponent_layout= QGridLayout(self.opponent_container)

        #Makes every row 1-5 have 100px
        for row in range(6):
            self.opponent_layout.setRowMinimumHeight(row, 100)

        #Makes every colmun 1-10 have 100px
        for col in range(11):
            self.opponent_layout.setColumnMinimumWidth(col, 100)


        #Buttons

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
                background: #008000;
                border: 2px solid #000000;
                border-radius: 3px;
            }

            QPushButton:hover {
                background: #339933;
            }
''')

        self.check= QPushButton('Check')
        self.check.setStyleSheet('''
            QPushButton {
                background: #FFD700;
                border: 2px solid #000000;
                border-radius: 3px;
            }

            QPushButton:hover {
                background: #FFE866;
            }
''')

        self.rise= QPushButton('Raise') 
        self.rise.setStyleSheet('''
            QPushButton {
                background: #4169E1;
                border: 2px solid #000000;
                border-radius: 3px;
            }

            QPushButton:hover {
                background: #6787E7;
            }
''')

        #Cards

        self.card_1= QPushButton()

        self.card_2= QPushButton()



        self.button_layout.addWidget(self.fold, 2, 1, alignment= Qt.AlignmentFlag.AlignBottom)
        self.button_layout.addWidget(self.call, 3, 1, alignment= Qt.AlignmentFlag.AlignTop)
        self.button_layout.addWidget(self.check, 2, 2, alignment= Qt.AlignmentFlag.AlignBottom)
        self.button_layout.addWidget(self.rise, 3, 2, alignment= Qt.AlignmentFlag.AlignTop)

        self.player_layout.addStretch(6)
        self.player_layout.addWidget(self.card_1)
        self.player_layout.addWidget(self.card_2)
        self.player_layout.addStretch(1)
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

        if self.dealer == True:
            self.dealer_path()
            self.dealer= False

        else:
            self.not_dealer_path()
            self.dealer= True

    def board_pass_out(self):
        self.board.append(self.cards[5], self.cards[6], self.cards[7])

    def dealer_path(self):
        self.three_button= True
        self.check.hide()
        
        self.button_layout.addWidget(self.fold, 2, 1, 1, 2, alignment= Qt.AlignmentFlag.AlignBottom)

        self.fold.clicked.connect(self.end_game)

        self.call.clicked.connect(self.bot_move)

        self.rise.clicked.connect(self.raise_amount)

    def end_game(self):
        if self.win == True:
            print('You won')

        else:
            print('You lost')

    def raise_amount(self):
        self.bot_react()

    def bot_react(self):
        print('j')

    def bot_move(self):
        print('h')

    def not_dealer_path(self):
        self.two_button= True
        self.fold.hide()
        self.call.hide()

        #Function has not been created yet. Look over notes when it is created
        # self.check.clicked.connect()

        #Function has not been created yet. Look over notes when it is created
        # self.rise.clicked.connect()

if __name__ == '__main__':
    main()