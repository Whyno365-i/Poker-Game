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