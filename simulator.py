"""
Author: Andronikos Giachanatzis Grammatikopoulos
Date: 01/2021
Description: This module is the central execution point of a Simulator for Finite Automata. It was developed as a
            university assignment during my fourth year in the University of Macedonia.
            This program is used to simulate custom Finite Automata, which can check the validity of any word
            provided by a user.
Usage: Prepare a file that follows the template in the description_template.txt. This file must contain the description
       of an automaton. Note that any epsilon-transition is identified by the @ character in the description file.
       After you prepare the file execute the simulator.py file. You will be prompted to enter the name of the file
       that contains the description of the automaton.
       After you enter a valid filename you will be prompted to enter the word to check its validity according to the
       provided automaton. After you press Enter the result concerning the validity of the word will be shown.
       After you see the result you can enter another word by answering yes, or exit the simulation by answering no to
       the final question.
"""


import graph as gr
VERBOSE = True

def printDescription(description_dict):
    '''
    Prints the description of the automaton as read from the description file.
    :param description_dict: The dictionary that has the description of the automaton.s
    :return: None.
    '''
    print ("[!] Total states:", description_dict["states_num"])
    print ("[!] Initial state:", description_dict["initial_state"])
    print ("[!] Final states number:", description_dict["final_states_num"])
    print ("[!] Final states:", description_dict["final_states"])
    print ("[!] Transitions number:", description_dict["transitions_num"])
    print("[!] Transitions: ", description_dict["transitions"])



def main():
    # read the description of the automaton from a given file
    # the dictionary that saves the description of the automaton
    description_dict = dict()
    while True:
        try:
            description_filename = input("Enter the name of the file containing the description: ")
            desc_file = open(description_filename)
        except FileNotFoundError:
            print("[-] File not found")
        else:
            break

    description_dict["states_num"] = int(desc_file.readline().replace("\n", ""))
    description_dict["initial_state"] = desc_file.readline().replace("\n", "")
    description_dict["final_states_num"] = int(desc_file.readline().replace("\n", ""))
    description_dict["final_states"] = desc_file.readline().replace("\n", "")
    description_dict["transitions_num"] = int(desc_file.readline().replace("\n", ""))

    description_dict["transitions"] = list()
    for i in range(description_dict["transitions_num"]):
        description_dict["transitions"].append(desc_file.readline().replace("\n", ""))
    desc_file.close()

    # print the description of the automaton
    printDescription(description_dict)

    graph = gr.Graph(description_dict)

    while True:
        # read input
        word = input("Enter the word: ")
        result = graph.traverse(word)

        if result:
            print(f"[+] The word {word} is valid")
        else:
            print(f"[+] The word {word} is not valid")

        choice = input("Do you want to add another word? y/n: ")
        print()
        if choice == 'n':
            break



if __name__ == "__main__":
    main()