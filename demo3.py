import random

def roll_dice(sides=6):
    """
    Simulate rolling a dice with a given number of sides.
    Returns a random integer between 1 and 'sides' (inclusive).
    """
    return random.randint(1, sides)

# Example usage:
if __name__ == "__main__":
    print("Rolled:", roll_dice())