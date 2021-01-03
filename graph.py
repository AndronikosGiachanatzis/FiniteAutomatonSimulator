import node as nd


class Graph:

    # input the description
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
            end = transition[2]
            # add the transition of the start node to the node

            n = self.searchNode(start)
            if n is None:
                print("[-] An error has occurred while searching for a node: NODE NOT FOUND")
                exit(1)
            n.addTransition(input_char, end)
        print()


    def searchNode(self, target):
        '''
        Searches the nodes o a graph for a given node that is identified by its name
        :param target (str): The name of the target node
        :return: The node if the node has been found found, or None if the node has not been found
        '''
        for n in self.nodes:
            if n.name == target:
                return n
        return None
