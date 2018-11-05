"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time
import tkinter
from tkinter import ttk

def main():
    #colorsensortest()
    #polygontest(5)
    arm_and_claw_test()

def colorsensortest():
    """ Runs YOUR specific part of the project """
    colors = [rb.Color.RED.value, rb.Color.WHITE.value, rb.Color.BLUE.value]
    robot = rb.Snatch3rRobot()
    print(time.localtime())
    robot.color_sensor.wait_until_intensity_is_greater_than(20)
    print(time.localtime())
    robot.color_sensor.wait_until_intensity_is_less_than(80)
    print(time.localtime())
    robot.color_sensor.wait_until_color_is_one_of(colors)
    print(time.localtime())
    robot.color_sensor.wait_until_color_is(rb.Color.WHITE.value)
    print(time.localtime())
def polygontest(n):
    robot = rb.Snatch3rRobot()
    for k in range(n):
        robot.drive_system.go_straight_inches(10)
        time.sleep(.5)
        robot.drive_system.spin_in_place_degrees(180-((180*(n-2))//n))
        time.sleep(.5)
        print(180-((180*(n-2)//n)))
def arm_and_claw_test():
    robot = rb.Snatch3rRobot()
    robot.arm.raise_arm_and_close_claw()
    robot.arm.calibrate()
    robot.arm.move_arm_to_position(69000000)

def project(n):
    robot = rb.Snatch3rRobot()
    root = tkinter.Tk()
    root.title("Project Game")
    root.bind('<a>', lambda event: turn_left(robot))
    screen = tkinter.Canvas(root, height=300, width=400)
    screen.grid()
    for k in range(n):
        coin = screen.create_oval(100 + 10 * k, 100 + 10 * k, 100 + 10 + 10 * k, 100 + 10 + 10 * k, fill='yellow')
    root.mainloop()

def turn_left(self):
    while True:
        self.drive_system.left_wheel.start_spinning(-100)
        self.drive_system.right_wheel.start_spinning(100)
        if keyboard.is_pressed('a') == False:
            self.drive_system.left_wheel.stop_spinning()
            self.drive_system.right_wheel.stop_spinning()
main()
