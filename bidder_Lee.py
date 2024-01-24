import random
class Bidder:
    '''Class representing bidder'''
    def __init__(self, num_users, num_rounds):
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.balance = 0
        self.previous_bid = {}
        self.other_bidders_bids = {b: {} for b in range(num_users)}
        self.bidder_id = None
        self.auction_winner = None

    def __repr__(self):
        return f"Bidder(num_users = {self.num_users}, num_rounds={self.num_rounds})"

    def __str__(self):
        return f"Bidder with {self.num_users} users and {self.num_rounds} rounds"

    def bid(self, user_id):
        '''Place bid for given user'''

        self.bidder_id = user_id

        #get previous bid
        previous_bid = self.previous_bid.get(user_id, 0)

        #check other bids 
        obb = self.other_bidders_bids.get(user_id, {})
        if obb:
            max_ob = max(obb.values(), default=0)
            if max_ob > previous_bid:
                second_highest_bid = max(bid for bid in obb.values() if bid < max_ob)
                current_bid = second_highest_bid + random.uniform(0.1,0.75)
            else:
                current_bid = previous_bid + random.uniform(0.1, 0.50)
        else:
            current_bid = previous_bid + random.uniform(0.1, 0.75)

        self.previous_bid[user_id] = current_bid

        return round(current_bid, 3)
    
    def notify(self, auction_winner, price, clicked):
        '''Notify if winner/loser, click/no click'''
        if auction_winner:
            if clicked:
                print(f"Congratulations! You won the auction and the user clicked on the ad")
                print(f"Winning Price: ${price: .2f}")
            else:
                print(f"Congratulations! You won the auction but the user did not click on the ad")
                print(f"Winning Price: ${price: .2f}")
        else: 
            print("You did not win the auction")
