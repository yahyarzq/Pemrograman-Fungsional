

def Jump(player):
    print ("{} Jump".format(player))


def Roll(player):
    print ("{} Roll".format(player))

def Display(func):
    def wrapper():
        value = func()
        print ("Player {}".format(value))
    return wrapper()

def Kick(player):
    print ("{} Kick".format(player))

def Punch(player):
    print ("{} Punch".format(player))


@Display
def Ryu():
    Player = "Ryu"
    Kick(Player)
    Jump(Player)
    Roll(Player)
    return Player

@Display
def Ken():
    Player = "Ken"
    Roll(Player)
    return Player

@Display
def ChunLi():
    Player = "ChunLi"
    Roll(Player)
    Kick(Player)
    Punch(Player)
    return Player



