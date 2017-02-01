from motor import motor
from collections import OrderedDict

TEXT_SEPARATOR = '..........'
TEXT_PROPELLER = 'Propeller'
LEFT_PROPELLER = 0
TOP_PROPELLER = 1
RIGHT_PROPELLER = 2
DOWN_PROPELLER = 3


class Copter(object):
    """Propellers are indexed in Anti-Clockwise direction starting from left."""

    def __init__(self, name, no_of_propellers):
        self.name = name
        self.propellers = []
        self.__upArrowCounter = 0
        self.__downArrowCounter = 0
        self.__leftArrowCounter = 0
        self.__rightArrowCounter = 0

        props = []
        for index in range(1, no_of_propellers + 1):
            props.append((TEXT_PROPELLER + '-' + index, ''))

        self.__keys = OrderedDict(props)
        for i in range(1, no_of_propellers + 1):
            propeller_instance = motor('Propeller' + str(i), 17, simulation=False)
            propeller_instance.setW(0)
            self.propellers.append(propeller_instance)

    def get_propellers(self):
        return self.propellers

    def gain_altitude(self):
        for propeller in self.propellers:
            propeller.setW(0)
            propeller.increaseW()

    def decline_altitude(self):
        for propeller in self.propellers:
            propeller.decreaseW()

    def get_keys(self):
        return self.__keys
