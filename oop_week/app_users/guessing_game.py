from random import randint

class GuessingGame():
    def __init__(self):
        self._answer = randint(1, 10)

    def user_answer(self):
        return int(input("Guess a number between 1 - 10: "))

    def result(self, usr_answer):
        if usr_answer == self._answer:
            print("You got it")
            return True
        elif usr_answer > self._answer: 
            print("Too High")
            return self.result(self.user_answer())
        elif usr_answer < self._answer: 
            print("Too Low")
            return self.result(self.user_answer())
        else:
            print("Broke the game")
            return True


guessing_game = GuessingGame()

guessing_game.result(guessing_game.user_answer())


        
