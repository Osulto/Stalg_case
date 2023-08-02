with open("machine_definition.txt", "r") as file:
    line = file.readline()

states = line.strip().split(',')
states_values = states

def two_way_automaton(input_string):
    current_state = 'q0'
    index = 0
    stack = ['Z']
    counts = {0: 0, 1: 0}
    while True:
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

        elif current_state == 'q1':
            if index < len(input_string):
                symbol = input_string[index]
                if symbol == '1':
                    index += 1
                    stack.pop()
                    print(current_state, index, stack)
                elif symbol == '2':
                    index = len(input_string)-1
                    current_state = 'q2'
                    print(current_state, index, stack)
                else:
                    return False
            else:
                break

        elif current_state == 'q2':
            if index < len(input_string):
                symbol = input_string[index]
                if symbol == '2':
                    index -= 1
                    stack.append('X')
                    print(current_state, index, stack)
                elif symbol == '1':
                    current_state = 'q3'
                    #print(current_state, index, stack)
                else:
                    return False
            else:
                break

        elif current_state == 'q3':
            if index < len(input_string):
                symbol = input_string[index]
                if symbol == '1':
                    index -= 1
                    stack.pop()
                    print(current_state, index, stack)
                elif symbol == '0' and len(stack) == 1:
                    print(current_state, index, stack)
                    return True
                else:
                    return False
            else:
                break

   #return current_state == 'q1' and index == len(input_string)
    #return stack[0] == 'Z' and index == 2


# Main code to test the automaton
if __name__ == "__main__":
    input_string = input("Enter the input string (consisting of '0's, '1's): ")
    if two_way_automaton(input_string):
        print("Accepted.")
    else:
        print("Not Accepted.")
