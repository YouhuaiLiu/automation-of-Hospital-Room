from gpio import *
from time import *
from environment import Environment

customWrite(1, 0)
customWrite(2, [0, 1])
isLoop = True
door_counter = 0

while isLoop:
    cardReader_o = digitalRead(0)
    cardReader_i = digitalRead(3)
    if door_counter == 0:
        if cardReader_o == 0:
            customWrite(1, 0)
            customWrite(2, [0, 1])
            customWrite(4, 0)
            sleep(1)
        elif cardReader_o != 0:
            customWrite(1, 2)
            customWrite(2, [1, 0])
            customWrite(4, 3)
            sleep(5)
            customWrite(2,[0,0])
            print(cardReader_o)
            door_counter += 1
            continue
    elif door_counter == 1:
        if cardReader_i != 0:
            customWrite(2,[1,0])
            sleep(5)
            customWrite(1, 0)
            customWrite(2, [0, 1])
            customWrite(4, 0)
            door_counter -= 1
            sleep(1)
        else:
        	sleep(1)
    else:
        sleep(1)
