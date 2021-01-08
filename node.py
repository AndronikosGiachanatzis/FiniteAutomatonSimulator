EMPTY_WORD = '@'

'''
    This class represents a Node (or State) that belongs to a graph of an automaton.
    It carries information concerning the name (identifier) of a Node, the state of the node (that is whether it is
    a starting, final or intermediate node and the transitions originating from this node.
'''
class Node:

    def __init__(self, name, state):
        '''
        Initializes the basic features of a specific node.
        :param name (String): The name by which this node is identified.
        :param state (String): A string describing whether this node is an initial, final or intermediate node.
        '''
        self.name = name
        self.state = state

        # each transition is added separately afterwards, during the parsing of the transitions
        self.transitions = dict()


    # add a transition to the current Node/State
    def addTransition(self, input_char, end):
        '''
        Adds a transition to the transitions dictionary, which originates from this node. A transition is represented
        using the input character that triggers this transition and the destination node (end) of the transition
        (edge of the graph).
        :param input_char (Character): The input character that triggers this transition.
        :param end (Node): The destination node of this transition.
        :return : This function doesn't return anything.
        '''
        if input_char not in self.transitions:
            self.transitions[input_char] = list()
        self.transitions[input_char].append(end)


    def getDestinations(self, character):
        '''
        Gets all the possible destinations of every transition that is triggered when a specific character is entered.
        :param character (Character): The character that triggers the transitions.
        :return (List): A list containing all the possible destination nodes. The list may be empty if there aren't any
                        possible destination nodes for this specific character.
        '''
        if character in self.transitions:
            return self.transitions[character]
        else:
            return []

    def __str__(self):
        '''
        Overrides the string method. Provides custom String representation for the node. It simply prints the name of
        the node by which it is identified.
        :return (String): The String representation of this node.
        '''
        return (f"Node: {self.name}")


    def getEDestinations(self):
        '''
        Gets all the possible destinations of every epsilon transition which originate from this node.
        :return (List): A list containing all the possible destination nodes. The list may be empty if there aren't any
                        possible destination nodes.
        '''
        nxt = list()
        if EMPTY_WORD in self.transitions:
            for t in self.transitions[EMPTY_WORD]:
                nxt.extend(t.getEDestinations())
                if t not in nxt:
                    nxt.append(t)
                nxt.reverse()
                return nxt
        else:
            return []