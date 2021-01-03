import graph as gr

def printDescription(description_dict):
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
            # desc_file = open(description_filename)
            desc_file = open("description.txt")
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




if __name__ == "__main__":
    main()