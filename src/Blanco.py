"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import rosebotics_new as rb2
import ev3dev.ev3 as ev3
import time



def proximity_test():

    print('Running!')
    infrared = rb2.InfraredAsProximitySensor(ir_sensor_port=ev3.INPUT_4)

    while True:

        if infrared.get_distance_to_nearest_object() < 20:
            ev3.Sound.beep().wait()
            ev3.Sound.speak("Object is close!").wait()
            break



def follow_black_circle():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    drive = robot.drive_system
    color = robot.color_sensor
    turn_right = True

    while True:
        # Moving forward until light is reflected
        drive.start_moving()
        color.wait_until_intensity_is_greater_than(10)

        # Try turning clockwise (to the right)
        counter = 0
        while True:

            if turn_right is True:
                drive.start_moving(100, 0)
            else:
                drive.start_moving(0, 100)

            # Runs if robot is back on black within 0.25 seconds (implying that robot is turning in right direction)
            if color.get_reflected_intensity() < 10:
                break

            # Runs if robot has not encountered black after 0.25 seconds in direction it's turning
            if counter > 0.5 and color.get_reflected_intensity() > 10:
                print('No black detected, turn around!')

                # Revert to original position
                if turn_right is True:
                    drive.move_for_seconds(1, -100, 0)
                else:
                    drive.move_for_seconds(1, 0, -100)

                # Changes direction to turn in the future
                if turn_right is True:
                    turn_right = False
                else:
                    turn_right = True
                print('Turn direction changed! Now turn_right is :', turn_right)

                # Turn for certain amount of time
                while True:
                    if turn_right is True:
                        drive.start_moving(100, 0)
                    else:
                        drive.start_moving(0, 100)

                    if color.get_reflected_intensity() < 10:
                        break

            counter = counter + 0.05
            print(counter, color.get_reflected_intensity())
            time.sleep(0.05)


proximity_test()
