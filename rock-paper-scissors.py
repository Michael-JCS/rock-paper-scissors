class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""

class GameRound:
    def __init__(self, answer):
        self.answer = answer
        self.endRound = False
        


class Game:
    def __init__(self):
        self.count = 0
        self.endGame = False
        self.participant = Participant(str(input("Enter Name: ")))
        self.secondParticipant = Participant(str(input("Enter Name: ")))

    def start_round(self):
        self.participant.choice = self.get_player_input(self.participant)
        self.secondParticipant.choice = self.get_player_input(self.secondParticipant)
        self.determine_winner()
        self.points_system()

    def get_player_input(self, participant):
        # Simple input validation for demonstration purposes
        valid_choices = ["rock", "paper", "scissors"]
        while True:
            choice = input(f"{participant}'s turn. Enter 'rock', 'paper', or 'scissors': ").lower()
            if choice in valid_choices:
                return choice
            else:
                print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

    def determine_winner(self):
        if self.participant.choice == self.secondParticipant.choice:
            print("It's a tie!")
        elif (
            (self.participant.choice == "rock" and self.secondParticipant.choice == "scissors") or
            (self.participant.choice == "paper" and self.secondParticipant.choice == "rock") or
            (self.participant.choice == "scissors" and self.secondParticipant.choice == "paper")
        ):
            print(f"{self.participant} wins!")
            self.participant.points += 1
        else:
            print(f"{self.secondParticipant} wins!")
            self.secondParticipant.points += 1

    def points_system(self):
        print(f"Points: Participant1: {self.participant.points} | Participant2: {self.secondParticipant.points}")

    def ask_to_continue(self):
        response = input("Do you want to continue playing? (yes/no): ").lower()
        return response == "yes"

# Example usage:
game = Game()
while not game.endGame:
    game.start_round() if game.ask_to_continue() else setattr(game, 'endGame', True)

