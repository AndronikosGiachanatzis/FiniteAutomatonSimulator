import node as nd

'''
    This class is used to modelize a graph that holds all information relevant to an automaton.
    It carries information concerning te total number of the states of a graph, the number of the final states, 
    which state is the initial and which are the final states as well as the transitions between states.
    Each state is modelized by the Node class in the node.py module and henceforth the terms Node and State will
    be used identically. 
    At any given moment only one instance of this class is expected to exist as the simulator accepts one description
    file of one automaton. 
'''
class Graph:

    def __init__(self, desc_dict):
        self.states_num = desc_dict["states_num"]
        self.initial_state = desc_dict["initial_state"]
        self.final_states_num = desc_dict["final_states_num"]
        self.final_states = desc_dict["final_states"].split()

        # create the nodes with the given information from above. Add the transitions individually later
        self.nodes = dict()
        for i in range(1, self.states_num + 1):
            state = "00"
            if str(i) == self.initial_state:
                state = "10"
            if str(i) in self.final_states:
                s = list(state)
                s[1] = "1"
                state = "".join(s)

            n = nd.Node(str(i), state)
            self.nodes[n] = n

        self.transitions_num = desc_dict["transitions_num"]


        transitions = desc_dict["transitions"]
        for t in transitions:
            transition = t.split()
            start = transition[0]
            input_char = transition[1]
            end = self.searchNode(transition[2])

            # add the transition of the starting/source node to the node destination
            n = self.searchNode(start)
            if n is None:
                print("[-] An error has occurred while searching for a node: NODE NOT FOUND")
                exit(1)
            n.addTransition(input_char, end)
        print()


    def searchNode(self, target):
        '''
        Searches the nodes o a graph for a given node that is identified by its name
        :param target (String): The name of the target node
        :return: The node if the node has been found found, or None if the node has not been found
        '''
        for n in self.nodes:
            if n.name == target:
                return n
        return None


    def getInitialNode(self):
        '''
        Searches for the initial/starting node of the graph.
        :return (Node): The initial node of the graph.
        '''
        return self.searchNode(self.initial_state)

    def traverse(self, word):
        '''
        Traverses a graph, starting from the initial node according to the user's input and checks whether the word
        entered is a word that the automaton accepts or not.
        :param word (String): The word that the user entered to be checked whether it's a valid word or not
        :return (Boolean): True if the word entered is a valid word. False if the word entered is invalid
        '''
        # keep a list of all the possible states that the automaton is in
        curr_states = list()

        # start traversing the automaton from the initial node
        init = self.getInitialNode()
        curr_states.append(init)
        valid = True

        nxt_e = list()
        nxt_e.extend(curr_states[0].getEDestinations())
        curr_states.extend(nxt_e)
        # traverse through the graph starting from the initial node
        for c in word:
            # get a list of the next nodes for a given character
            nxt = list()
            tmp_curr = curr_states.copy()
            for s in tmp_curr:

                nxt.extend(curr_states[0].getDestinations(c))

                # remove the current node from the current states
                curr_states.pop(0)

            # if there is not a possible destination from all the current nodes, the word is not valid
            if nxt == [] and nxt_e == []:
                valid = False
                break

            # add the destinations to the possible current states
            curr_states.extend(nxt)

            if len(curr_states) > 0:
                nxt_e = list()
                nxt_e.extend(curr_states[0].getEDestinations())
                curr_states.extend(nxt_e)
            else:
                break


        # check if there weren't any destination nodes
        if valid:
            # check if any of the last current states is a final state
            for n in curr_states:
                if n.state[1] == '1':
                    return True
            # if none of the current states is a final node then the word is not valid
            return False
        else: # if there weren't any next nodes return False, the word isn't valid
            return False
