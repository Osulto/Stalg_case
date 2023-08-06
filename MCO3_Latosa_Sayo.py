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

        current_state = trans[0]
        read = trans[1]
        pop = trans[2]
        direction = trans[3]
        nxtstate = trans[4]
        push = trans[5]

        symbol = input_string[index]

        while symbol == read and index < len(input_string):
            symbol = input_string[index]
            if index < len(input_string) and symbol == read:

                if direction == 'R':
                    index += 1
                elif direction == 'L':
                    index -= 1
                elif direction == '0':
                    index = index

                if pop != '@':
                    if len(stack) >= 1:
                        stack.pop()

                if push != '@' and symbol == read:
                    stack.append(push)
            else:
                break

            print('Current State:', current_state)
            print('String Char:', symbol)
            print('Direction:', direction)
            print('Stack:', stack)
            print('================================')

    if len(stack) == 1:
        return True


# Main code to test the automaton
if __name__ == "__main__":
    input_string = input("Enter a string consisting of 0's and 1's \n put a '>' by the end of it: ")
    if two_way_automaton(input_string):
        print("[ACCEPTED STRING]")
    else:
        print("[INVALID STRING]")

"""""
Text File Format:
States: q0,q1,q2,q3
Inputs: 0,1
Initial State: q0
Final State: q3
Transitions q0,0,@,R,q0,X:
Current State | Read | Pop | Direction | Next State | Push
"""""
