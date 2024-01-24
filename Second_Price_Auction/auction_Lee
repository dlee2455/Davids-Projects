import random

class User:
    '''Class representing a user '''
    def __init__(self):
        self.__probability = random.uniform(0,1)

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def show_ad(self):
        '''a show_ad method with the definition def show_ad(self) that represents showing an ad
        to this User . This method should return True to represent the user clicking on and ad and
        False otherwise.'''
        return random.uniform(0,1) < self.__probability

class Auction:
    '''Class auction represents running the auction. Attributes of users and bidders '''

    def __init__(self, users, bidders):
        self.users = users
        self.bidders = bidders
        self.balances = {bidder_idx: 0 for bidder_idx in range(len(bidders))}

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self)

    def execute_round(self):
        #Select random user
        user = random.choice(self.users)

        #Get bids
        bids = {}
        for bidder in self.bidders:
            bids[bidder] = bidder.bid(user)

        #Get highest bid
        highest_bid = max(bids.values(), default=0)

        #Get Winner value (Higest Bidder)
        winner = max(bids, key=bids.get)
        winning_price = bids.get(winner)

        #Check for ties in highest bidders (aka more than 1 highest bidder)
        tie_bidders = [bidder for bidder in bids if bids[bidder] == winning_price]
        #If tie, select random winner
        if len(tie_bidders) > 1: 
            winner = random.choice(tie_bidders)

        #Get #2 
        if len(bids)>1:
            sorted_bids = sorted(bids.values(), reverse=True)
            second_highest_bid = sorted_bids[1]
        else:
            second_highest_bid = 0
   
        #Show Ad
        clicked = user.show_ad()

        #Notify Winning Bidder about outcome of the auction
        for bidder in self.bidders:
            bidder_idx = self.bidders.index(bidder)
            if bidder == winner:
                winner.notify(True, second_highest_bid, clicked)
                self.balances[bidder_idx] -= second_highest_bid
                if clicked:
                    self.balances[bidder_idx] += 1
                pass
            else:
                bidder.notify(False, second_highest_bid, None)




