with open("machine_definition.txt", "r") as file:
    states = file.readline()
    inputs = file.readline()
    initial = file.readline()
    final = file.readline()
    transition = [line.strip().split(',') for line in file]

states = states.strip().split(',')
inputs = inputs.strip().split(',')
def two_way_automaton(input_string):
    current_state = 'q0'
    stack = ['Z']
    index = 0

    for trans in transition:

        read = trans[1]
        current_state = trans[0]
        pop = trans[2]
        direction = trans[3]
        nxtstate = trans[4]
        push = trans[5]

        if current_state == nxtstate:
            next = nxtstate
        else:
            next = current_state

        symbol = input_string[index]

        if index < len(input_string) :
            print('before', symbol)
            if index != len(input_string)-1:
                index += 1
            print('after:', symbol)













    """""""""
    if next == current_state:
        while index < len(input_string):
            symbol = input_string[index]
            print('symbol:', symbol)
            print('read', read)
            print('index', index)
            print('===========================')
            if symbol != read:
                break
            else:
                if pop != '@':
                    print('POP')
                    stack.pop()

                if direction == '1':
                    index += 1

                elif direction == '0':
                    index = index

                elif direction == '-1':
                    index -= 1

                if push != '@':
                    stack.append(push)

        print('state:', current_state, stack)
"""""""""

# Main code to test the automaton
if __name__ == "__main__":
    input_string = input("Enter the input string (consisting of '0's, '1's): ")
    if two_way_automaton(input_string):
        print("Accepted.")
    else:
        print("Not Accepted.")
