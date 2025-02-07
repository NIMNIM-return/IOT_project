import numpy as np


class Sensor:
    def __init__(self, name, group, unit):
        self.name = name

        self.group = group

        self.unit = unit

    def read_sensor(self):
        return np.random.uniform(20, 25)

class Device:
    def __init__(self,topic,status):
        self.status = status

        self.topic = topic

        self.topic_list = topic.split('/')

        self.location = self.topic_list[0]

        self.group = self.topic_list[1]

        self.device_type = self.topic_list[2]

        self.name = self.topic_list[3]

#baraye in ke befahmim aya roshan hast ya na
    def turn_on(self):
        if self.status == 'on' or 'On' or 'ON':
            print ('it is on already!')
        elif self.status == 'off' or 'Off' or 'OFF':
            self.status = 'on'
            print('it is on now')

    def turn_off(self):
        if self.status == 'off' or 'Off' or 'OFF':
            print ('it is off already!')
        elif self.status == 'on' or 'On' or 'ON':
            self.status = 'off'
            print('it is off now')
    def show_status(self):
        return self.status


if __name__=='__main__':
    a1=Device('home/living room/lamp/lamp1', 'on')
    a1.turn_on()