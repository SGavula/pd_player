import random

class MyPlayer:
    ''' A player that analysis matrix and chooses the best strategy '''

    COOPERATE = False
    DEFECT = True

    def __init__(self, payoff_matrix, number_of_iterations = None):
        #Initialization of variables
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.history_of_opponent = []
        self.answer = None
        self.my_last_move = None
        self.opponent_last_move = None
        self.best_strategy = None
        #Initialization of variables for single round
        self.coop = self.payoff_matrix[0][0][0] + self.payoff_matrix[0][1][0]
        self.defect = self.payoff_matrix[1][0][0] + self.payoff_matrix[1][1][0]
        #Initialization of variables for more rounds
        self.always_coop = self.payoff_matrix[0][0][0] + self.payoff_matrix[0][0][1]
        self.always_change = self.payoff_matrix[0][1][0] + self.payoff_matrix[0][1][1]
        self.always_def = self.payoff_matrix[1][1][0] + self.payoff_matrix[1][1][1]

        #Check if we'll be playing one round or more rounds and select strategy
        if number_of_iterations == 1:
            if self.coop > self.defect:
                self.answer = self.COOPERATE
            else:
                self.answer = self.DEFECT
        else:
            if self.always_coop > self.always_change and self.always_coop > self.always_def:
                self.answer = self.COOPERATE
                self.best_strategy = "always_coop"

            if self.always_change > self.always_coop and self.always_change > self.always_def:
                self.answer = random.choice((self.COOPERATE, self.DEFECT))
                self.best_strategy = "always_change"

            if self.always_def > self.always_coop and self.always_def > self.always_change:
                self.answer = self.DEFECT
                self.best_strategy = "always_defect"
    
    def move(self):
        #Check if in the array history of opponent exists at least one element
        if(len(self.history_of_opponent)):
            self.opponent_last_move = self.history_of_opponent[len(self.history_of_opponent) - 1]

            if(len(self.history_of_opponent) == 1):
                if(self.best_strategy == "always_coop"):
                    if (self.my_last_move, self.opponent_last_move) != (self.COOPERATE, self.COOPERATE):
                        self.answer = self.COOPERATE
                elif(self.best_strategy == "always_defect"):
                    if (self.my_last_move, self.opponent_last_move) != (self.DEFECT, self.DEFECT):
                        self.answer = self.DEFECT
            else:
                self.answer = self.opponent_last_move
            
            if(self.best_strategy == "always_change"):
                if (self.my_last_move, self.opponent_last_move) in (( self.DEFECT, self.COOPERATE) , (self.COOPERATE, self.DEFECT)):
                    self.answer = self.opponent_last_move
                else:
                    self.answer = random.choice((self.COOPERATE, self.DEFECT))

        if(self.answer == None):
            self.answer = random.choice((self.COOPERATE, self.DEFECT))

        return self.answer

    def record_last_moves(self, my_last_move, opponent_last_move):
        self.my_last_move = my_last_move
        #Check if array historz of opponent has more than 10 elements, if so, remove the first element from array
        if len(self.history_of_opponent) >= 10:
            self.history_of_opponent.pop(0)
        self.history_of_opponent.append(opponent_last_move)


if __name__ == "__main__":
    p1 = MyPlayer( ( ((2,2),(2,2)) , ((2,2),(2,2)) ), 1)
    result = p1.move()
    print(result)