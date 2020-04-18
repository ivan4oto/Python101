class BowlingGame:
    def __init__(self, strikeslist):
        self.strikeslist = strikeslist
        self._frames = 10
        self._scoreboard = []

    def write(self,score):
        self._scoreboard.append(score)

    def frame(self): 
        roll1 = self.strikeslist.pop(0)
        roll2 = 0
        if roll1 < 10:
            roll2 = self.strikeslist.pop(0)
            #if we have a spare
            if (roll1 + roll2) == 10:
                roll2 += self.strikeslist[0]
                #if spare in last frame, clears strikelist for error checking
                if self._frames == 1:
                    self.strikeslist = []
                
        elif roll1 == 10:
            roll1 += (self.strikeslist[0] + self.strikeslist[1])
            #if strike in last frame, clears strikelist for error checking
            if self._frames == 1:
                self.strikeslist = []

        return roll1 + roll2

    def play(self):
        while self._frames > 0:
            if len(self.strikeslist) < 2:
                raise ValueError('Input is wrong')
            self.write(self.frame())
            self._frames -= 1
            
        if len(self.strikeslist) > 0:
            raise ValueError('Input is wrong')

    def result(self):
        return (sum(self._scoreboard))

def main():
    pass

if __name__ == "__main__":
    main()


        






