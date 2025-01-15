'''
A farmer has a goat, a wolf and a cabbage on the west side of a
river. He wants to get all of his animals and his cabbage across
the river onto the east side. The farmer has a row boat but he only
has enough room for himself and one other thing. The wolf will eat
the goat if they are left together alone. The goat will eat the
cabbage if they are left together alone. How can the farmer get
everything on the east side?
i) Formulate this puzzle as search
ii) Solve this problem-using search (any method)
iii) Draw the search tree and show the final solution
'''
#          "F"  "G"  "C"  "W"
initial = ('E', 'E', 'E', 'E')
goal =    ('W', 'W', 'W', 'W')

def transitions(curr):
    X = 'E'
    if curr[0] == 'E':
        X = 'W'
    
    
    return {
        (X, curr[1], curr[2], curr[3]),
        (X,     X, curr[2], curr[3]),
        (X, curr[1],     X, curr[3]),
        (X, curr[1], curr[2],     X),
    }

def gameover(state, start):
    # goat with cabbage when farmer is absent
    if state[1] == state[2] and state[1] != state[0]:
        return True
    # goat with wolf when farmer is absent
    if state[1] == state[3] and state[1] != state[0]:
        return True
    # if start and current state is same also gameover (stoping the infinite loop)
    if state == start:
        return True
    return False

def play(start, goal):
    curr = start
    while curr != goal:
        states = transitions(curr)
        # filter states using constraints or gameover check
        for state in states:
            if gameover(state, start):
                # remove state from states
                states.remove(state)
        
        
