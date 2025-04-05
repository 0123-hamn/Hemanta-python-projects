import random
class SnakeWaterGunGame:
    def __init__(self):
        self.choices = ["snake", "water", "gun"]
    
    def get_computer_choice(self):
        """Randomly selects a choice for the computer."""
        return random.choice(self.choices)

    def determine_winner(self, user, computer):
        """Determines the winner based on the game rules."""
        if user == computer:
            return "It's a Tie!"
        elif (user == "snake" and computer == "water") or \
             (user == "water" and computer == "gun") or \
             (user == "gun" and computer == "snake"):
            return "You Win! 🎉"
        else:
            return "Computer Wins! 🤖"
    def play(self):
        """Runs the game in a loop until the user wants to exit."""
        print("Welcome to Snake-Water-Gun Game! 🐍💦🔫")
        while True:
            user_choice = input("\nEnter your choice (snake/water/gun) or 'quit' to exit: ").lower() 
            if user_choice == "quit":
                print("Thanks for playing! 👋")
                break
            if user_choice not in self.choices:
                print("Invalid choice! Please enter 'snake', 'water', or 'gun'.")
                continue
            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            result = self.determine_winner(user_choice, computer_choice)
            print(result)

# Run the game
game = SnakeWaterGunGame()
game.play()
