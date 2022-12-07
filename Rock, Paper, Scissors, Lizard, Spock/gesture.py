from time import sleep


class Gesture:
    def __init__(self) -> None:
        self.name = ''
        self.gesture_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.gesture_chosen = ''


    def pick_gesture(self):
        correct_choice = False
        while correct_choice is False:
            num_choice = int(input('Choose gesture: '))
            sleep(1)
            if num_choice == 0 or num_choice == 1 or num_choice == 2 or num_choice == 3 or num_choice == 4:
               self.gesture_chosen = self.gesture_list[num_choice]
               correct_choice = True
            else:
                print('Please select correct gesture!') 
                sleep(1)
                correct_choice = False
        return self.gesture_chosen