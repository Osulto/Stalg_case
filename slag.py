def two_way_automaton(input_string):
    current_state = 'q0'
    index = 0
    #count_0 = 0
    #count_1 = 0


    while True:
        if current_state == 'q0':
            if index < len(input_string):
                symbol = input_string[index]
                if symbol == '0':
                    #count_0 += 1
                    index += 1
                    print(current_state, index)
                elif symbol == '1':
                    #count_1 += 1
                    index += 1
                    current_state = 'q1'
                    print(current_state, index)
                else:
                    return False
            else:
                break

        elif current_state == 'q1':
            if index < len(input_string):
                symbol = input_string[index]
                if symbol == '0':
                    #count_0 += 1
                    index += 1
                    print(current_state, index)
                elif symbol == '1':
                    #count_1 += 1
                    index -= 1
                    current_state = 'q2'
                    print(current_state, index)
                else:
                    return False
            else:
                break

        elif current_state == 'q2':
            if index < len(input_string):
                symbol = input_string[index]
                if symbol == '0':
                    index += 1
                    current_state = 'q0'
                    print(current_state, index)
                elif symbol == '1':
                    #count_1 += 1
                    index -= 1
                    print(current_state, index)
                else:
                    return False
            else:
                break
    return current_state == 'q1' and index == len(input_string)


# Main code to test the automaton
if __name__ == "__main__":
    input_string = input("Enter the input string (consisting of '0's, '1's): ")
    if two_way_automaton(input_string):
        print("Accepted.")
    else:
        print("Not Accepted.")
