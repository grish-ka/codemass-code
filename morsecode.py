# MIT License

# Copyright (c) 2025 grish-ka

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from machine import Pin
from utime import sleep

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-' }


led = Pin("LED", Pin.OUT)
red = Pin(18, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher

def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                if citext:
                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                    .values()).index(citext)]
                citext = ''
    return decipher.strip()

def startup():
    led.on()
    sleep(1)
    red.on()
    sleep(1)
    yellow.on()
    sleep(1)
    green.on()
    sleep(1)
    led.off()
    red.off()
    yellow.off()
    green.off()

if __name__ == "__main__":
    try:
        startup()
        message = "HELLO WORLD"
        result = encrypt(message)
        print (result)
        for symbol in result:
            if symbol == '.':
                led.on()
                red.on()
                sleep(0.2)
                led.off()
                red.off()
            elif symbol == '-':
                led.on()
                yellow.on()
                sleep(0.6)
                led.off()
                yellow.off()
            else:
                sleep(0.6)  # Space between letters
            sleep(0.2)  # Space between symbols
        green.on()
        print("Message \"%s\" transmitted in Morse code." % decrypt(result))
        sleep(5)
        green.off()

    except KeyboardInterrupt:
        print ("Transmission interrupted.")
        led.off()
        red.off()
        yellow.off()
        green.off()
        red.on()
        sleep(3)
        yellow.on()
        green.on()
        led.on()
        sleep(5)
        red.off()
        yellow.off()
        green.off()