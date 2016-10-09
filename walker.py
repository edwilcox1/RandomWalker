from random import randint
class Walker(object):
    
    def __init__(self):
        self.x = width/2
        self.y = height/2
        self.walks = []
        self.total = 0
    
    def walk(self):
       self.total += 1
       for i in range(1, len(self.walks)):
           self.walks[i-1] = self.walks[i]
       moves = (randint(-1, 1), randint(-1, 1))
       self.x += moves[0]
       self.y += moves[1]
       self.walks.append((self.x, self.y))
    def show(self):
        #fill(255)
        #stroke(255)
        for walk in self.walks:
            ellipse(walk[0], walk[1], 8, 8)