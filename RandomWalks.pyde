from walker import Walker
walkers = []
def setup():
    size(400, 400)
    
    for count in xrange(5):
        x = Walker()
        walkers.append(x)

def draw():
    background(0)
    for walker in walkers:
        walker.walk()
        walker.show()