import rosebotics_new as rb
import ev3dev.ev3 as ev3
import mqtt_remote_method_calls as com
import time

def main():
    """

    type: rb.Snatch3rRobot
    """
    print('running')
    speed = 100
    robot = rb.Snatch3rRobot()
    remote = Remote(robot, speed)
    client = com.MqttClient(remote)
    client.connect_to_pc()
    while True:
        pass

class Remote(object):
    def __init__(self, robot, speed):
        """
        Stores the robot
        :type robot: rb.Snatch3rRobot
        """
        self.robot = robot
        self.speed = speed
        self.hits = 0

    def go_forward(self):
        self.robot.drive_system.go_straight_inches(1, self.speed)

    def turn_left(self):
        self.robot.drive_system.spin_in_place_degrees(90, -100)

    def go_backward(self):
        self.robot.drive_system.go_straight_inches(1, -self.speed)

    def turn_right(self):
        self.robot.drive_system.spin_in_place_degrees(90)

    def you_win(self):
        ev3.Sound.play('/home/robot/csse120/assets/kirby.wav')

    def check_speed(self):
        if self.robot.proximity_sensor.get_distance_to_nearest_object() < 10:
                self.hits += 1
                self.speed = self.speed - 10 * self.hits

        if self.hits == 4:
                ev3.Sound.set_volume(200)
                ev3.Sound.play('/home/robot/csse120/assets/sounds/kirbylose.wav').wait()
main()