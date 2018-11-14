"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time
import random
import tkinter
import keyboard
import mqtt_remote_method_calls as com
from tkinter import ttk

class State(object):
    def __init__(self,screen,n):
        self.direction = 0
        self.hits = 0
        self.coins_collected = 0
        self.text = screen.create_text(175,10,text=str(n-1)+' coins remain!')
class Coin(object):
    def __init__(self,screen):
        self.x = random.randint(5, 391)
        self.y = random.randint(5, 291)
        self.existence = screen.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill='yellow')
        self.gottenness = False

def main():
    #colorsensortest()
    #polygontest(5)
    #arm_and_claw_test()
    project()

########################
# def colorsensortest():
#     """ Runs YOUR specific part of the project """
#     colors = [rb.Color.RED.value, rb.Color.WHITE.value, rb.Color.BLUE.value]
#     robot = rb.Snatch3rRobot()
#     print(time.localtime())
#     robot.color_sensor.wait_until_intensity_is_greater_than(20)
#     print(time.localtime())
#     robot.color_sensor.wait_until_intensity_is_less_than(80)
#     print(time.localtime())
#     robot.color_sensor.wait_until_color_is_one_of(colors)
#     print(time.localtime())
#     robot.color_sensor.wait_until_color_is(rb.Color.WHITE.value)
#     print(time.localtime())
# def polygontest(n):
#     robot = rb.Snatch3rRobot()
#     for k in range(n):
#         robot.drive_system.go_straight_inches(10)
#         time.sleep(.5)
#         robot.drive_system.spin_in_place_degrees(180-((180*(n-2))//n))
#         time.sleep(.5)
#         print(180-((180*(n-2)//n)))
# def arm_and_claw_test():
#     robot = rb.Snatch3rRobot()
#     robot.arm.raise_arm_and_close_claw()
#     robot.arm.calibrate()
#     robot.arm.move_arm_to_position(69000000)
########################
def project():
    root = tkinter.Tk()
    root.title("Project Game")
    n=2
    client = com.MqttClient()
    client.connect_to_ev3()
    screen = tkinter.Canvas(root, height=300, width=400)
    screen.grid()
    state = State(screen,n)
    char = screen.create_oval(0,0,15,15, fill='red')
    coin1 = Coin(screen)
    # coin2 = Coin(screen)
    # coin3 = Coin(screen)
    # coin4 = Coin(screen)
    # coin5 = Coin(screen)
    # listnew = [coin1, coin2, coin3, coin4, coin5]
    listnew = [coin1]
    root.bind('<w>', lambda event: go_forward(client,screen,char,state,n,listnew,state.text))
    root.bind('<a>', lambda event: turn_left(client,state))
    root.bind('<s>', lambda event: go_backward(client,screen,char,state,n,listnew,state.text))
    root.bind('<d>', lambda event: turn_right(client,state))
    screen.update()
    root.mainloop()


def go_forward(client,screen,char,state,n,listnew,text):
    if state.coins_collected <= n-1:
        client.send_message('check_speed')
        time.sleep(.1)
        client.send_message('go_forward')
        if state.direction == 0:
            screen.move(char,1,0)
        elif state.direction == 1:
            screen.move(char,0,1)
        elif state.direction == 2:
            screen.move(char,-1,0)
        elif state.direction == 3:
            screen.move(char,0,-1)
        for k in range(n-state.coins_collected+1):
            if listnew[k].gottenness == False:
                    if ((screen.coords(char)[0] >=
                            screen.coords(listnew[k].existence)[0] and
                            screen.coords(char)[0] <=
                            screen.coords(listnew[k].existence)[2]
                            and screen.coords(char)[1]
                            >= screen.coords(listnew[k].existence)[1] and
                            screen.coords(char)[1] <=
                            screen.coords(listnew[k].existence)[3]) or (screen.coords(char)[2] >=
                            screen.coords(listnew[k].existence)[0] and
                            screen.coords(char)[2] <=
                            screen.coords(listnew[k].existence)[2]
                            and screen.coords(char)[3]
                            >= screen.coords(listnew[k].existence)[1] and
                            screen.coords(char)[3] <=
                            screen.coords(listnew[k].existence)[3])) :
                        listnew[k].gottenness = True
                        state.coins_collected += 1
                        screen.delete(listnew[k].existence)
                        screen.delete(state.text)
                        state.text = screen.create_text(175,10,text=str(n-1-state.coins_collected)+' coins remain!')
                        screen.update()
                        break
        if state.coins_collected == n-1:
            you_win(client)
            screen.delete(text)
            text = screen.create_text(175,10,text='You win!')
            time.sleep(1)
            screen.delete(screen)
        game_over(client)


def turn_left(client,state):
    client.send_message('check_speed')
    time.sleep(.1)
    client.send_message('turn_left')
    if state.direction == 0:
        state.direction = 3
    elif state.direction == 3:
        state.direction = 2
    elif state.direction == 2:
        state.direction = 1
    elif state.direction == 1:
        state.direction = 0



def go_backward(client,screen,char,state,n,listnew,text):
    client.send_message('check_speed')
    time.sleep(.1)
    client.send_message('go_backward')
    time.sleep(.01)
    if state.direction == 0:
        screen.move(char,-1,0)
    if state.direction == 1:
        screen.move(char,0,-1)
    if state.direction == 2:
        screen.move(char,1,0)
    if state.direction == 3:
        screen.move(char,0,1)
    for k in range(n - state.coins_collected + 1):
        if listnew[k].gottenness == False:
            if ((screen.coords(char)[0] >=
                 screen.coords(listnew[k].existence)[0] and
                 screen.coords(char)[0] <=
                 screen.coords(listnew[k].existence)[2]
                 and screen.coords(char)[1]
                 >= screen.coords(listnew[k].existence)[1] and
                 screen.coords(char)[1] <=
                 screen.coords(listnew[k].existence)[3]) or (screen.coords(char)[2] >=
                                                             screen.coords(listnew[k].existence)[0] and
                                                             screen.coords(char)[2] <=
                                                             screen.coords(listnew[k].existence)[2]
                                                             and screen.coords(char)[3]
                                                             >= screen.coords(listnew[k].existence)[1] and
                                                             screen.coords(char)[3] <=
                                                             screen.coords(listnew[k].existence)[3])):
                listnew[k].gottenness = True
                state.coins_collected += 1
                screen.delete(listnew[k].existence)
                screen.delete(state.text)
                state.text = screen.create_text(175, 10, text=str(n - 1 - state.coins_collected) + ' coins remain!')
                screen.update()
                break
    if state.coins_collected == n - 1:
        you_win(client)
        screen.delete(text)
        text = screen.create_text(175, 10, text='You win!')
        time.sleep(1)
        screen.delete(screen)
    game_over(client)

def turn_right(client,state):
    client.send_message('check_speed')
    time.sleep(.1)
    client.send_message('turn_right')
    if state.direction == 0:
        state.direction = 1
    elif state.direction == 1:
        state.direction = 2
    elif state.direction == 2:
        state.direction = 3
    elif state.direction == 3:
        state.direction = 0

def you_win(client):
    client.send_message('you_win')
def game_over(client):
    client.send_message('game_over')
main()
