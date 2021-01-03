class Node:

    def __init__(self, name, state):
        self.name = name
        self.state = state

        # each transition is added separately afterwards, during the parsing of the transitions
        self.transitions = dict()


    # add a transition to the current Node/State
    def addTransition(self, input_char, end):
        if input_char not in self.transitions:
            self.transitions[input_char] = list()
        self.transitions[input_char].append(end)


