"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time
import random
import tkinter
import keyboard
import paho.mqtt
from tkinter import ttk
from ev3dev import ev3

def main():
    #colorsensortest()
    #polygontest(5)
    #arm_and_claw_test()
    project(5)

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
def project(n):
    robot = rb.Snatch3rRobot()
    robot.beacon_sensor.get_distance_to_beacon()
    #root = tkinter.Tk()
    #root.title("Project Game")
    #screen = tkinter.Canvas(root, height=300, width=400)
    #screen.grid()
    #root.bind('<w>', lambda event: go_forwards(robot))
    #root.bind('<w>', lambda event: print('forward'))
    # root.bind('<a>', lambda event: turn_left(robot))
    #root.bind('<a>', lambda event: print('left'))
    # root.bind('<s>', lambda event: go_backwards(robot))
    #root.bind('<s>', lambda event: print('backwards'))
    # root.bind('<d>', lambda event: turn_right(robot))
    #root.bind('<d>', lambda event: print('right'))
    #char = screen.create_oval(0,0,15,15, fill='red')
    coins_remaining = n
    # for k in range(n):
    #     coinx = random.randint(5,391)
    #     coiny = random.randint(5,291)
    #     coin = screen.create_oval(coinx, coiny, coinx+10, coiny+10, fill='yellow')
    # screen.update()
    if coins_remaining == 0:
        you_win(robot)
    #root.mainloop()


def go_forward(self):
    while True:
        self.drive_system.left_wheel.start_spinning(100)
        self.drive_system.right_wheel.start_spinning(100)
        if keyboard.is_pressed('w') == False:
            self.drive_system.left_wheel.stop_spinning()
            self.drive_system.right_wheel.stop_spinning()
            break

def turn_left(self):
    while True:
        self.drive_system.left_wheel.start_spinning(-100)
        self.drive_system.right_wheel.start_spinning(100)
        if keyboard.is_pressed('a') == False:
            self.drive_system.left_wheel.stop_spinning()
            self.drive_system.right_wheel.stop_spinning()
            break

def go_backward(self):
    while True:
        self.drive_system.left_wheel.start_spinning(-100)
        self.drive_system.right_wheel.start_spinning(-100)
        if keyboard.is_pressed('s') == False:
            self.drive_system.left_wheel.stop_spinning()
            self.drive_system.right_wheel.stop_spinning()
            break

def turn_right(self):
    while True:
        self.drive_system.left_wheel.start_spinning(100)
        self.drive_system.right_wheel.start_spinning(-100)
        if keyboard.is_pressed('d') == False:
            self.drive_system.left_wheel.stop_spinning()
            self.drive_system.right_wheel.stop_spinning()
            break

def you_win(self):
    ev3.Sound.play('/home/robot/csse120/assets/sounds/kirby.wav')
    ev3.Sound.speak('You Win').wait()

main()
