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
        """
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

        if index < len(input_string):
            symbol = input_string[index]
            if symbol == read and symbol == '0':

                if current_state == 'q1' and read == '2':
                    index = len(input_string)-1

                if direction == '1':
                    index += 1
                elif direction == '-1':
                    index -= 1
                else:
                    index = index

                if push != '@':
                    stack.append(push)

                if pop != '@':
                    stack.pop()

                next_state = nxtstate
                print(current_state,index,stack)

            elif symbol == read and symbol == '1':

                if current_state == 'q1' and read == '2':
                    index = len(input_string) - 1

                if direction == '1':
                    index += 1
                elif direction == '-1':
                    index -= 1
                else:
                    index = index

                if push != '@':
                    stack.append(push)

                if pop != '@':
                    stack.pop()

                next_state = nxtstate
                print(current_state, index, stack)

            if symbol == read and symbol == '2':

                if current_state == 'q1' and read == '2':
                    index = len(input_string)-1

                if direction == '1':
                    index += 1
                elif direction == '-1':
                    index -= 1
                else:
                    index = index

                if push != '@':
                    stack.append(push)

                if pop != '@':
                    stack.pop()

                next_state = nxtstate
                print(current_state,index,stack)



# Main code to test the automaton
if __name__ == "__main__":
    input_string = input("Enter the input string (consisting of '0's, '1's): ")
    if two_way_automaton(input_string):
        print("Accepted.")
    else:
        print("Not Accepted.")
