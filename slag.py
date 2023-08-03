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
    index = 0
    stack = ['Z']
    for trans in transition:
        current_state = trans[0]
        read = trans[1]
        pop = trans[2]
        direction = trans[3]
        nxtstate = trans[4]
        push = trans[5]

        if current_state == nxtstate:
            next = nxtstate
        else:
            next = current_state

        if next == current_state :
            if index < len(input_string):
                symbol = input_string[index]
                if symbol == read:
                    if pop != '@':
                        stack.pop()
                    if direction == '1':
                        index += 1
                    elif direction == '0':
                        index = index
                    elif direction == '-1':
                        index -= 1


                    if push != '@':
                        stack.append(push)
            print(current_state, index, stack)

    """
    print('next:',next,'\n','current state:', current_state)
            if current_state == 'q0':
                if index < len(input_string):
                    symbol = input_string[index]
                    if symbol == '0':
                        index += 1
                        stack.append('X')
                        print(current_state, index, stack)
                    elif symbol == '1':
                        current_state = 'q1'
                    else:
                        return False
                else:
                    break
            """





# Main code to test the automaton
if __name__ == "__main__":
    input_string = input("Enter the input string (consisting of '0's, '1's): ")
    if two_way_automaton(input_string):
        print("Accepted.")
    else:
        print("Not Accepted.")
