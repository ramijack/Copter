# importing modules
import motor
from collections import OrderedDict

TEXT_SEPARATOR = '..........'
TEXT_PROPELLER = 'Prop'


class Copter(object):
    """Propellers are indexed in Anti-Clockwise direction starting from left."""

    def __init__(self, name, no_of_propellers):
        self.name = name
        self.propellers = []
        self.__counters = [0] * no_of_propellers
        props = []
        for index in range(0, no_of_propellers):
            propeller_instance = motor.motor(TEXT_PROPELLER + str(index), 17, simulation=False)
            propeller_instance.setW(0)
            self.propellers.append(propeller_instance)
            props.append((TEXT_PROPELLER + '-' + str(index), ''))

        self.__keys = OrderedDict(props)

    def get_propellers(self):
        return self.propellers

    def gain_altitude(self):
        for propeller in self.propellers:
            propeller.setW(0)
            propeller.increaseW()

        for index in range(0, len(self.propellers)):
            self.__counters[index] += 1
            self.__keys[TEXT_PROPELLER + '-' + str(index)] = TEXT_PROPELLER + '-' + str(index) + TEXT_SEPARATOR + \
                "%s" % self.__counters[index]

    def decline_altitude(self):
        for propeller in self.propellers:
            propeller.decreaseW()

        for index in range(0, len(self.propellers)):
            self.__counters[index] -= 1
            self.__keys[TEXT_PROPELLER + '-' + str(index)] = TEXT_PROPELLER + '-' + str(index) + TEXT_SEPARATOR + \
                "%s" % self.__counters[index]

    def get_keys(self):
        return self.__keys

    def change_propeller_rotation_speed(self, index, accelerate):
        if accelerate:
            self.propellers[index].increaseW()
            self.__counters[index] += 1
        else:
            self.propellers[index].decreaseW()
            self.__counters[index] -= 1

        self.__keys[TEXT_PROPELLER + '-' + str(index)] = TEXT_PROPELLER + '-' + str(index) + TEXT_SEPARATOR + \
            "%s" % self.__counters[index]

    def reset_acceleration(self):
        for index in range(0, len(self.__counters)):
            self.__counters[index] = 0

        for key in self.__keys:
            self.__keys[key] = ''
