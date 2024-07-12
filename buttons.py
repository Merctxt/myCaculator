from typing import TYPE_CHECKING
import math
from PySide6.QtWidgets import QPushButton, QGridLayout, QMessageBox
from PySide6.QtCore import Slot
from path import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber, convertToNumber



if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow


class Buttom(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)

class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow',
                 *args, **kwargs):
        super().__init__(*args, **kwargs) 

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],
        ]

        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equationInitialValue = 'sua conta'
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)


    def _makeGrid(self):
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)
        
        for row_number, rowData in enumerate(self._gridMask):
            for column_number,  button_text in enumerate(rowData):
                button = Buttom(button_text)

                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, row_number, column_number)
                slot = self._makeSlot(self._insertToDisplay, button_text)
                self._connectButtonClicked(button, slot)


    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()
        
        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text in '+-/*^':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._configLeftOp, text)
                )
            
        if text == '=':
            self._connectButtonClicked(button, self._eq)

        if text == '◀':
            self._connectButtonClicked(button, self.display.backspace)

        if text == 'N':
            self._connectButtonClicked(button, self._negative)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot()
        def realSlot():
            func(*args, **kwargs)
        return realSlot
    
    @Slot()
    def _negative(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return
        
        newNumber = convertToNumber(displayText) * -1
        self.display.setText(str(newNumber))
        



    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return
        
        self.display.insert(text)
        self.display.setFocus()
        
    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _configLeftOp(self, text):
        displayText = self.display.text()
        self.display.clear()
        self.display.setFocus()

        if not isValidNumber(displayText) and self._left is None:
            self._showError('Conta incompleta!')
            return
        
        if self._left is None:
            self._left = convertToNumber(displayText)


        self._op = text
        self.equation = f'{self._left} {self._op} ??'

        
    @Slot()
    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._left is None:
            self._showError('Conta incompleta!')
            return
        
        self._right = convertToNumber(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'
        
        try:
            if '^' in self.equation and isinstance(self._left, int |float):
                result = math.pow(self._left, self._right)
                result = convertToNumber(str(result))
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError(
                'Não é possível fazer uma divisão por 0.',
                "A divisão por zero não pode ser definida porque "
                "não há um número que, multiplicado por zero, "
                "resulte em um número diferente de zero.")
        except OverflowError:
            self._showError(
                'Não foi possível realizar a conta',
                'Este número é tão grande que vai além da'
                ' compreensão de seu computador :D')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None
        self.display.setFocus()

        if result == 'error':
            self._left = None

    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    def _showError(self, text, informative_text=None):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Question)


        okButton = msgBox.addButton(QMessageBox.Ok) #type: ignore
        okButton.setText('OK')

        cancelButton = msgBox.addButton(QMessageBox.StandardButton.Cancel)
        cancelButton.setText('Cancelar')

        if informative_text:
            msgBox.setInformativeText(informative_text)

        msgBox.exec()
        self.display.setFocus()
        
        