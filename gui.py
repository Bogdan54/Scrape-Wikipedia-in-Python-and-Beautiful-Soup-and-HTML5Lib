import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from subprocess import Popen

class WikiGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Wikipedia Search')
        self.setGeometry(100, 100, 400, 200)

        # Create search label and input field
        self.search_label = QLabel(self)
        self.search_label.setText('Enter search term:')
        self.search_label.move(20, 20)
        self.search_input = QLineEdit(self)
        self.search_input.move(150, 20)
        self.search_input.resize(200, 20)

        # Create URL label and input field
        self.url_label = QLabel(self)
        self.url_label.setText('Enter Wikipedia URL:')
        self.url_label.move(20, 60)
        self.url_input = QLineEdit(self)
        self.url_input.move(150, 60)
        self.url_input.resize(200, 20)

        # Create search button
        self.search_button = QPushButton('Search', self)
        self.search_button.move(150, 100)
        self.search_button.clicked.connect(self.run_wiki_script)

    def run_wiki_script(self):
        search_term = self.search_input.text()
        url = self.url_input.text()

        if search_term:
            cmd = ['python ', 'wiki.py ', '--search', search_term]
        elif url:
            cmd = ['python', 'wiki.py', '--url', url]
        else:
            return

        with open('output.txt', 'w') as f:
            process = Popen(cmd, stdout=f, stderr=f)
            process.wait()

        # Open the output file in a new window
        os.startfile('output.txt')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WikiGUI()
    ex.show()
    sys.exit(app.exec_())