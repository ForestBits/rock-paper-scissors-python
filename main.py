import random

#player is the "avatar" entity - it can be controled by human or CPU
class Player:
    pass

class PlayerType:
    HUMAN = 0
    CPU = 1

class StatusType:
    STANDING = 0

class Action:
    def __init__(self, name, required_status, resulting_status, time_cost, damage, target_status):
        self.name = name
        self.required_status = required_status
        self.resulting_status = resulting_status
        self.time_cost = time_cost
        self.damage = damage
        self.target_status = target_status

actions = [
    Action(name = "Hit",
           required_status = StatusType.STANDING,
           resulting_status = StatusType.STANDING,
           time_cost = 1,
           damage = 1,
           target_status = StatusType.STANDING),
    Action(name = "Big Hit",
           required_status = StatusType.STANDING,
           resulting_status = StatusType.STANDING,
           time_cost = 2,
           damage = 2,
           target_status = StatusType.STANDING)
]

"""

gets the actions the player can choose, taking into account status and time left this turn

"""
def get_available_actions_for_player(player):
    time_left = TIME_UNITS_PER_TURN - get_action_list_time_cost(player.action_list)

    # we figure out what our state WILL be after executing every action in the list
    # if we have no actions yet, the status for the purpose of move selection is the current status
    # else, our current status is the resulting status of the last move chosen
    if len(player.move_list) == 0:
        last_status = player.status
    else:
        last_status = player.move_list[-1].resulting_status

    possible_actions = []

    for action in actions:
        if action.required_status == last_status and action.time_cost <= time_left:
            possible_actions.append(action)

    return possible_actions


def print_action_list(action_list):
    for action in action_list:
        damaging = action.damage > 0

        index = 1

        if damaging:
            print("({0}) {1} - {2} damage, takes {3} time units".format(
                  index, action.name, action.damage, action.time_cost))
        else:
            print("({0}) {1} - takes {2} time units".format(index, action.name, action.time_cost))

        ++index

def get_action_list_time_cost(action_list):
    time_cost = 0

    for action in action_list:
        time_cost += action.time_cost

    return time_cost

"""
this function gets moves 1 after the other for the specified player, using the appropriate
behavior function.

get_action is a function which retrieves the next action chose from the respective (player, cpu...) source.
it takes args:
    player - player object
    action_list - moves that are available for this turn
"""
def get_player_actions(player, get_action):
    return [actions[0], actions[0], actions[0]]

    # clear previous actions
    player.action_list = []

    while True:
        time_taken = get_action_list_time_cost(action_list)

        if time_taken == TIME_UNITS_PER_TURN:
            break

        available_actions = get_available_actions_for_player(player)

        next_action = get_action(available_actions)

        action_list.append(next_action)


def get_human_action(player, action_list):
    while True:
        print("Chose your next action:")

        print_action_list(action_list)

        print("\nType the name or number of the action":)

def get_cpu_action(player, action_list):
    return action_list[random.randomint(0, len(action_list) - 1)]

"""
    get_player_actions(player)

    get_cpu_actions(enemy)

    player_action_index = 0
    cpu_action_index = 0

    for current_time_unit in range(0, TIME_UNITS_PER_TURN):

        """

def print_game_result(p1, p2):
    p1Win = p2.health <= 0
    p2Win = p1.health <= 0

    # draw
    if p1Win and p2Win:
        print("{0} and {1} both died! Draw!".format(p1.full_name, p2.full_name))

    elif p1Win:
        print("{0} has defeated {1}!".format(p1.full_name, p2.full_name))

    elif p2Win:
        print("{0} has defeated {1}!".format(p2.full_name, p1.full_name))


def run_game(p1, p2):
    while True:
        if p1.health <= 0 or p2.health <= 0:
            print_game_result(p1, p2)

            return

        run_round(p1, p2)

def run_round(p1, p2):
    p1.status = StatusType.STANDING
    p2.status = StatusType.STANDING

    # get player's actions from respective input source
    p1.action_list = get_player_actions(p1, p1.type == PlayerType.HUMAN ? get_human_action : get_cpu_action)
    p2.action_list = get_player_actions(p2, p2.type == PlayerType.HUMAN ? get_human_action : get_cpu_action)

    for current_time_unit in range(0, TIME_UNITS_PER_TURN):
        run_time_slice(p1, p2)

        if p1.health <= 0 or p2.health <= 0:
            return

def run_time_slice(p1, p2):

    p1HasAction = p1.time_unit_delay == 0
    p2HasAction = p2.time_unit_delay == 0

    # both players execute an action this turn
    if p1HasAction and p2HasAction:
        execute_simultaneous_actions(p1, p2)

    # only p1 is executing an action; p2 is in the middle of an action
    elif p1HasAction:
        execute_one_sided_action(p1, p2)

    # only p2 is executing an action; p1 is in the middle of an action
    elif p2HasAction:
        execute_one_sided_action(p2, p1)

def execute_simultaneous_actions(p1, p2):
    p1Action = p1.action_list[0]

    del p1.action_list[0]

    p2Action = p2.action_list[0]

    del p2.action_list[0]

    p1.status = p1Action.resulting_status


def execute_one_sided_action(acting_player, delayed_player):
    action = acting_player.action_list[0]

    del acting_player.action_list[0]

    acting_player.status = action.resulting_status
    acting_player.time_unit_delay =
    #big hit hits at the end, not the beginning. All damage moves hit at end?

    if action.damage > 0:
        # action does damage, we must check if it hit
        if action.target_status == delayed_player.status:
            # player takes damage and is disrupted out of their current action
            delayed_player.health -= action.damage
            delayed_player.status = StatusType.STANDING
            delayed_player.time_unit_delay = 0


name_jokes = [
    "You poor thing...",
    "What were your parents thinking...",
    "Not the sharpest name in the shed, I must say.",
    "Ha! But I guess people laugh at you a lot, with a name like that.",
    "I wouldn't even name my poodle that."
]

enemy_titles = [
    "Sir",
    "Squire",
    "Knight",
    "Swordsman",
    "King",
    "Guardian",
    "Earl",
    "Prince"
]

enemy_names = [
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


name = "Jacob" #get_name()

print("")

print("Your name is {0}?\n{1}\n".format(name, name_jokes[random.randint(0, len(name_jokes) - 1)]))

enemy_title = enemy_titles[random.randint(0, len(enemy_titles) - 1)]
enemy_name = enemy_names[random.randint(0, len(enemy_names) - 1)]
enemy_full_name = enemy_title + " " + enemy_name

print("Your enemy is {0}.".format(enemy_full_name))

START_HEALTH = 5
TIME_UNITS_PER_TURN = 3

player = Player()

player.type = PlayerType.HUMAN
player.name = name
player.full_name = name
player.health = START_HEALTH
player.status = StatusType.STANDING
player.action_list = []
player.time_unit_delay = 0

enemy = Player()

enemy.type = PlayerType.CPU
enemy.name = enemy_name
enemy.full_name = enemy_full_name
enemy.health = START_HEALTH
enemy.status = StatusType.STANDING
enemy.action_list = []
enemy.time_unit_delay = 0



run_game(player, enemy)
