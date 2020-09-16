# Add your Python code here. E.g.
from microbit import *
import random

# Variables for the script.
# x is main script, y is games script and z is if night light is on or not.
x=1
y=0
z=0
while x == 1:
    display.scroll('Hello')


# main menu

    display.scroll('A GAMES')
    display.scroll('B NIGHT LIGHT')
    x += 1
while x == 2:
    if button_a.is_pressed():
        y += 1
        x += 1
    elif button_b.is_pressed():
        display.scroll('NIGHT LIGHT ON')
        z += 1
        x += 1
    
while y == 1:
    display.scroll('LETS PLAY')
    display.scroll('A = 8 BALL')
    display.scroll('B = ROCK PAPER SICCOR')
    display.scroll('A + B MAIN MENU')
    y += 1

while y == 2:
    if button_a.is_pressed():
        display.scroll('8 BALL')
        y += 1
    elif button_b.is_pressed():
        display.scroll('ROCK PAPER SICCOR')
        y += 2
    elif button_b.is_pressed() and button_a.is_pressed():
        y = 0
        x = 2
    
        
    


while z == 1:
    if display.read_light_level() < 10:
        display.show(Image(
        "99999:"
        "90009:"
        "99999:"
        "90009:"
        "99999"))
    else:
        display.clear()
    sleep(2000)

while y == 3:
    if accelerometer.was_gesture('shake'):
        tool = random.randint(0,2)
        if tool == 0:
            display.show(Image.SQUARE_SMALL)
        elif tool == 1:
            display.show(Image.SQUARE)
        else:
            display.show(Image.SWORD)
    if button_b.is_pressed() and button_a.is_pressed():
        y = 0
        x = 2


while y == 4:
    if accelerometer.was_gesture('shake'):
        number = random.randint(1, 4)

        if number == 3:
            display.show(Image.YES)
        elif number == 2:
            display.show(Image.NO)
        elif number == 4:
            diplay.show(Image.HEART)
        else:
            display.show(Image.MEH)
    if button_b.is_pressed() and button_a.is_pressed():
        y = 0
        x = 2

        


