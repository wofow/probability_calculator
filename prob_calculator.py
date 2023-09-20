# Import necessary modules
import copy
import random

# Define a class named Hat
class Hat:
    # Constructor method to initialize the Hat object with balls of different colors and quantities
    def __init__(self, **balls):
        self.contents = []  # Initialize an empty list to represent the contents of the hat
        # Iterate through the provided balls dictionary and add balls to the contents list
        for ball, count in balls.items():
            self.contents.extend([ball] * count)

    # Method to draw a specified number of balls from the hat
    def draw(self, num_balls):
        # If the requested number of balls is greater than or equal to the number of balls in the hat,
        # return a copy of all the balls and leave the hat empty
        if num_balls >= len(self.contents):
            return self.contents.copy()

        # Otherwise, randomly sample without replacement from the contents of the hat to simulate drawing
        drawn_balls = random.sample(self.contents, num_balls)

        # Remove the drawn balls from the hat's contents
        for ball in drawn_balls:
            self.contents.remove(ball)

        return drawn_balls

# Function to perform experiments and calculate the probability of a certain outcome
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_draws = 0  # Initialize a counter for successful draws

    # Repeat the experiments a specified number of times
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)  # Create a deep copy of the hat to not modify the original
        drawn_balls = hat_copy.draw(num_balls_drawn)  # Draw a specified number of balls

        # Count the occurrences of each drawn ball
        drawn_balls_count = {ball: drawn_balls.count(ball) for ball in set(drawn_balls)}

        success = True  # Initialize a flag for success

        # Check if the drawn balls match the expected ball counts
        for ball, count in expected_balls.items():
            if ball not in drawn_balls_count or drawn_balls_count[ball] < count:
                success = False
                break

        if success:
            successful_draws += 1  # Increment the successful draw counter

    probability = successful_draws / num_experiments  # Calculate the probability of success
    return probability

if __name__ == "__main__":
    hat = Hat(black=6, red=4, green=3)  # Create a Hat object with specified ball quantities
    probability = experiment(hat=hat,
                             expected_balls={"red": 2, "green": 1},  # Define the expected ball counts
                             num_balls_drawn=5,  # Specify the number of balls to be drawn
                             num_experiments=2000)  # Specify the number of experiments

    print(f"Estimated probability: {probability:.4f}")  # Print the estimated probability
