import random

def roll_dice(sides=6):
    """Simulate rolling a dice with a given number of sides."""
    return random.randint(1, sides)

def pretty_print(message):
    """Print a message with some formatting."""
    print("=" * 30)
    print(message)
    print("=" * 30)

def generate_random_insult():
    """Generate a random insult."""
    insults = [
        "You have the charisma of a damp rag.",
        "If brains were dynamite, you wouldn't have enough to blow your nose.",
        "You're not stupid; you just have bad luck thinking."
    ]
    return random.choice(insults)

