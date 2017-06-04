import random


name_jokes = [
    "You poor thing...",
    "What were your parents thinking...",
    "Not the sharpest name in the shed, I must say.",
    "Ha! But I guess people laugh at you a lot, with a name like that.",
    "I wouldn't even name my poodle that."
]

opponent_titles = [
    "Sir",
    "Squire",
    "Knight",
    "Swordsman",
    "King",
    "Guardian",
    "Earl",
    "Prince"
]

opponent_names = [
    "Tim",
    "Dominick",
    "Morton",
    "Nathan",
    "Maxwell",
    "Cornelious",
    "Roland",
    "Frances",
    "Watson",
    "Carlton",
    "Olin",
    "Mathias",
    "Ferdinand",
    "Evan",
    "Phillip",
    "Paul",
    "Simon"
]


def print_intro():
    print("Welcome to the stabbing game!\n")

def get_name():
    print("Do tell, what is your name?")

    while True:
        name = input("Name: ")

        if len(name) < 3:
            print("Your name is too short, I am afraid.\n")
        else:
            return name





print_intro()


name = get_name()

print("")

print("Your name is {0}?\n{1}\n".format(name, name_jokes[random.randint(0, len(name_jokes) - 1)]))

opponent_title = opponent_titles[random.randint(0, len(opponent_titles))]
opponent_name = opponent_names[random.randint(0, len(opponent_names))]
opponent_full_name = opponent_title + " " + opponent_name

print("Your enemy is {0}".format(opponent_full_name))
