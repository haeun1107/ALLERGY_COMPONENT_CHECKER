from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from menu import Menu
from show_ import Show


# class Button - 버튼의 이름과 콜백 함수를 리턴 받아 이벤트 핸들러 함수 호출
class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)


# class ComponentSearch - UI component
class ComponentSearch(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Buttons and Edit
        self.searchButton = Button('Search', self.buttonClicked)
        self.clearButton = Button('C', self.buttonClicked)
        self.previousButton = Button('<-', self.buttonClicked)
        self.nextButton = Button('->', self.buttonClicked)

        self.searchEdit = QLineEdit()
        self.consolEdit = QTextEdit()
        self.consolEdit.setReadOnly(True)
        self.nonconsolEdit = QLineEdit()
        self.nonconsolEdit = QTextEdit()
        self.nonconsolEdit.setReadOnly(True)
        self.pictureEdit = QLabel()

        self.pixmap = QPixmap()
        self.pixmap.load('default.jfif')
        self.name = 'default.jfif'
        self.picture = self.pixmap.scaled(400, 400)
        self.pictureEdit.setPixmap(self.picture)

        # Grid Creation and Placement
        pictureLayout = QGridLayout()
        searchLayout = QGridLayout()
        consolLayout = QGridLayout()
        nonconsolLayout = QGridLayout()
        nextLayout = QGridLayout()

        pictureLayout.addWidget(self.pictureEdit, 1, 0, 4, 1)
        searchLayout.addWidget(self.searchEdit, 1, 2)
        searchLayout.addWidget(self.searchButton, 1, 3)
        searchLayout.addWidget(self.clearButton, 1, 4)
        consolLayout.addWidget(self.consolEdit, 2, 2, 3, 4)
        nonconsolLayout.addWidget(self.nonconsolEdit, 4, 2, 5, 4)
        nextLayout.addWidget(self.previousButton, 5, 0)
        nextLayout.addWidget(self.nextButton, 5, 1)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addLayout(pictureLayout, 1, 0, 4, 1)
        mainLayout.addLayout(nextLayout, 5, 0, 5, 1)
        mainLayout.addLayout(searchLayout, 1, 2, 1, 4)
        mainLayout.addLayout(consolLayout, 2, 2, 3, 4)
        mainLayout.addLayout(nonconsolLayout, 4, 2, 5, 4)

        self.setLayout(mainLayout)

        self.setWindowTitle("Allergy Component Checker")

        self.startCheck()

    # menu의 클래스인 Menu의 객체 생성, show_의 클래스인 Show의 객체 생성
    def startCheck(self):
        self.menu = Menu()
        self.show_ = Show()

    # 이벤트 처리 담당 함수
    def buttonClicked(self):
        component = self.searchEdit.text()  # 사용자가 입력한 값
        key = self.sender().text()  # 어떤 버튼이 눌렸는지

        if key == 'Search':
            try:
                result = ''
                non_result = ''
                if component in self.menu.components_list:  # 사용자가 검색한 성분이 해당되는 음식이 있다면,
                    self.name_result, self.comp_result, self.noname_result, self.nocomp_result = self.show_.showConsol(
                        component)
                    result += "해당 성분을 포함한 음식" + "\n" * 2
                    non_result += "해당 성분을 포함하지 않는 음식" + "\n" * 2
                    for a in range(len(self.name_result)):
                        result += (self.name_result[a] + " : ")
                        for b in self.comp_result[a]:
                            result += b + ", "
                        result += "\n" * 2
                    for c in range(len(self.noname_result)):
                        non_result += (self.noname_result[c] + " : ")
                        for d in self.nocomp_result[c]:
                            non_result += d + ", "
                        non_result += "\n" * 2

                else:  # 없다면 오류 발생 (except로)
                    raise
                self.consolEdit.setText(str(result))
                self.nonconsolEdit.setText(str(non_result))
            except:  # 에러처리 - QMessageBox 이용하여 안내 후 모든 입력 초기화
                QMessageBox.warning(self, "입력을 초기화 합니다.", '해당 성분을 포함한 음식이 존재하지 않습니다.')
                self.searchEdit.setText('')
        elif key == '<-':  # 메뉴판 순서의 역순으로 사진 띄우기
            self.imgNames = ['13.png', '12.png', '11.png', '10.png', '9.png', '8.png',
                             '7.png', '6.png', '5.png', '4.png', '3.png', '2.png', '1.png', 'default.jfif']
            for i in range(len(self.imgNames)):
                if self.name == self.imgNames[i]:
                    previous_file_name = self.imgNames[0 if len(self.imgNames) - 1 == i else i + 1]
                    self.pixmap.load(previous_file_name)
                    self.picture = self.pixmap.scaled(200, 200)
                    self.pictureEdit.setPixmap(self.picture)
                    self.name = previous_file_name
                    break
        elif key == '->':  # 메뉴판 순서와 맞게 사진 띄우기
            self.imgNames = ['default.jfif', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png',
                             '8.png', '9.png', '10.png', '11.png', '12.png', '13.png']
            for i in range(len(self.imgNames)):
                if self.name == self.imgNames[i]:
                    next_file_name = self.imgNames[0 if len(self.imgNames) - 1 == i else i + 1]
                    self.pixmap.load(next_file_name)
                    self.picture = self.pixmap.scaled(400, 400)
                    self.pictureEdit.setPixmap(self.picture)
                    self.name = next_file_name
                    break
        elif key == 'C':  # 모든 입력 초기화
            self.searchEdit.setText('')


# Main
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    search = ComponentSearch()
    search.show()
    sys.exit(app.exec_())
