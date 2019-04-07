import RPi.GPIO as GPIO
import time
from tkinter import *


## MORSE CODE DICTIONARY ##
CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

## SET UP ##
ledPin=8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin,GPIO.OUT, initial=GPIO.LOW)

## GUI DEFINITIONS ##
win = Tk()
win.title("LED Morse Code")

## EVENT FUNCTIONS ##
def dot():
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(ledPin,GPIO.LOW)
    time.sleep(0.2)

def dash():
    GPIO.output(ledPin,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(ledPin,GPIO.LOW)
    time.sleep(0.2)

def morseCode():
        word = entry.get()
        for letter in word:
            for symbol in CODE[letter.upper()]:
                if symbol == '-':
                    dash()
                elif symbol == '.':
                    dot()
                else:
                    time.sleep(0.5)
            time.sleep(0.5)

## WIDGETS ##
label = Label(win, text="User Name")
label.grid(row=5, column=0)

entry = Entry(win, bd =5)
entry.grid(row=5, column=1)

morseButton=Button(win, text='Morse Code', command=morseCode, height=1, width=6)
morseButton.grid(row=5, column=2)

exitButton=Button(win, text='Exit', command=quit, height=1, width=6)
exitButton.grid(row=6, column=1)

win.mainloop()