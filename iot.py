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

class AdminPanel:
    def __init__(self):
        self.groups={}

    def create_group(self, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f'group {group_name} is created')
        else:
            print('your name is duplicated')

    def add_device_to_group(self, group_name, device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            print('your device added to the group')
        else:
            print('your group is not created yet')

    def create_device(self, group_name, device_type, name):
        if group_name in self.groups:
            topic = f'home/{group_name}/{device_type}/{name}'
            new_device = Device(topic,status='off')
            self.add_device_to_group(group_name, new_device)
            print( F'device {name} is created')
        else:
            print('your group is not created')

    def create_multiple_devices(self, group_name, device_type, number_of_devices):
        if group_name in self.groups:
            for i in range(1, number_of_devices + 1):
                device_name = f'{device_type}{i}'
                topic = f'home/{group_name}/{device_type}/{device_name}'
                new_device = Device(topic,status='off')
                self.add_device_to_group(group_name, new_device)
            print (f'{number_of_devices}{device_type} has been cerated')
        else:
            print('your group is not created yet')

    def get_devices_in_groups(self, group_name):
        if group_name in self.groups:
            return self.groups[group_name]
        else:
            print(f'there is no group named: {group_name}')

    def turn_on_all_in_groups(self, group_name):
        devices = self.get_devices_in_groups(group_name)
        for device in devices:
            device.turn_on()
        print(f'all devises in {group_name} is now turned on')

    def turn_off_all_in_groups(self, group_name):
        devices = self.get_devices_in_groups(group_name)
        for device in devices:
            device.turn_off()
        print(f'all devises in {group_name} is now turned off')

            
if __name__=='__main__':
    a1=Device('home/living room/lamp/lamp1', 'on')
    a1.turn_on()
