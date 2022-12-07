from player import Player
from time import sleep
from gesture import Gesture

class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.type = 'human'
        self.name = name

    def display_gestures(self):
        counter = 0
        print(f'{self.name}, choose between these options: ')
        for gesture in self.gestures:
            print(f'Choose {str(counter)} for {gesture}')
            sleep(1)
            counter += 1


    def gesture_update(self):
        self.display_gestures()
        self.gesture = Gesture()
        self.choice_of_gesture = self.gesture.pick_gesture()