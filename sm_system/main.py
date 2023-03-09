# Created package files using script
import sys
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton


# For testing only
# Replace this class with the exact project
class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        # Create widgets
        self.name_label = QLabel('Name: ')
        name_line_edit = QLineEdit()

        self.birthdate_label = QLabel('Date of birth MM/DD/YYYY: ')
        self.date_of_birth = QLineEdit()

        calculate_btn = QPushButton('Calculate Age')
        calculate_btn.clicked.connect(self.calculate_age)
        self.output_label = QLabel('')

        # Add widgets to grid
        grid.addWidget(self.name_label, 0, 0,)
        grid.addWidget(name_line_edit, 0, 1,)
        grid.addWidget(self.birthdate_label, 1, 0,)
        grid.addWidget(self.date_of_birth, 1, 1,)
        grid.addWidget(calculate_btn, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        current_yr = datetime.now().year
        date_of_birth = self.date_of_birth.text()
        year_of_birth = datetime.strptime(date_of_birth, '%m/%d/%Y').date().year
        age = current_yr - year_of_birth
        self.output_label.setText(f'{self.name_label} is {age} years-old')


def main():
    app = QApplication(sys.argv)
    age_calculator = AgeCalculator()
    age_calculator.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
