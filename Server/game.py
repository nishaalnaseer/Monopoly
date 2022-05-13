from random import randint

class Player:
    def __init__(self, ip, username, password, landOnGoDoubled=False):
        """ init for palyer instance"""

        # network and profile info
        self.info = [username, ip, password]

        # player info
        self.cash = 1500
        self.state = 0  # minimum 0 and 40 something
        self.debted = False  # if player is debted he shouldnt be able to play
        self.houses = 0  # number of houses
        self.hotels = 0  # number of hotels
        self.jailFreeCards = 0  # number of JFs
        self.jailed = False  # if in jail = true
        self.landOnGoDoubled = landOnGoDoubled  # if set to true, when a player land on go go pass is paid
        self.properties = []

    def transaction(amount):
        """function for any transaction sets a flag if player is indebted"""
        self.cash += amount
        if self.cash < 0:
            self.debted = True
    
    def updateState(amount):
        """function to update the state of player or the position of the player
        readjust the state to between 39 and 0
        go pass is normally paid only after go is passed but if 
        landOnGoDoubled is set to true go pass is also paid at state 0, and 1
        """

        for x in range(amount):
            self.state += 1

            if self.state == 40 and landOnGoDoubled == True:
                transaction(200)  # add 200 to cash

            if self.state == 41:
                transaction(200)  # add 200 to cash

        if self.state > 39:
            self.state -= 40
        elif self.state < 0:
            self.state += 40

    def updateInfo(username, ip, password):
        """in the event of a ip change, password change or username change this
        may be updated"""
        self.info = [username, ip, password]
    
    def jailStatusInverted():
        """function to if jailed, then player is not jailed, if not jaield player gets jailed"""
        self.jailed = not self.jailed

    def backwardsUpdate(pos):
        self.state = pos

class Game:
    def __init__(self):
        """init game"""
        self.playerCount = 0  # number of players in game
        self.players = {}  # data struct for players
        self.doubledTimes = 0  # variable for the amount of times a player has doubles
        self.turnCounter = 0  # a counter to decide whos turn it is
    
    def addPlayers(self, ip, username, password):
        """function to add players, the player id is their index at join"""
        playerName = f"player{self.playerCount}"
        self.players.update({playerName: Player(ip, username, password)})

        self.playerCount += 1
    
    def playDice(self):
        """randomes value for dice"""
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)

        if dice1 == dice2:
            self.doubledTimes += 1
        
        return [dice1 , dice2]
    
    def turn():
        self.currentPlayer = f'player{turnCounter}'

        roll = playDice()

        if self.doubledTimes == 3:
            playerJailed()

        self.turnCounter += 1

        if self.turnCounter > self.playerCount:
            self.turnCounter -= self.playerCount
        
        return roll
    
    def playerJailed():
        players[currentPlayer].jailStatusInverted()
        players[currentPlayer].backwardsUpdate(10)