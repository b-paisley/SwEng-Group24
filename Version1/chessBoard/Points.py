class points:
    def __init__(self):
        self.player_w_points=-39
        self.player_b_points=-39

    def change_w_points(self,val:int):
        self.player_w_points+=val
        
    def change_b_points(self,val:int):
        self.player_b_points+=val