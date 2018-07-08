import math

print("welcome to fibonacci sequence maker 3000!\n")
sequence = []


def suffix_grabber(num):
    num = num % 10
    if num == 1:
        return "st"
    elif num == 2:
        return "nd"
    elif num == 3:
        return "rd"
    else:
        return "th"


def find_num(seek):
    global sequence
    curr_place = round(len(sequence) / 2)
    up_bound = len(sequence) - 1
    low_bound = 0
    iterations = 0
    worst_scenario = math.log(len(sequence))
    while True:
        if iterations > worst_scenario:
            if seek > sequence[up_bound]:
                print("that value is larger than any number in the "
                      "sequence, the closest is", sequence[up_bound], "\n")
            elif seek < sequence[low_bound]:
                print("that value is smaller than any number in the "
                      "sequence, the closest is", sequence[low_bound], "\n")
            else:
                print("The value you specified was not found "
                      "the closest values are {0} and {1}\n"
                      .format(sequence[low_bound], sequence[up_bound]))
            break
        elif seek < sequence[curr_place]:
            up_bound = curr_place
            curr_place = round((low_bound + curr_place) / 2)
        elif seek > sequence[curr_place]:
            low_bound = curr_place
            curr_place = round((up_bound + curr_place) / 2)
        else:
            print("The the value of {0} is the {1}{2} element in the sequence"
                  .format(seek, curr_place + 1, suffix_grabber(curr_place+1)), "\n")
            break
        iterations += 1
        '''print(sequence[up_bound])
        print(sequence[low_bound])'''


def ground_control():
    global sequence
    while True:
        usr_choice = input("how many more numbers do you want to add?"
                           " you can type 'seq' to see the current sequence,"
                           "'quit', 'search' to find one element or 'redo' to make a "
                           "new sequence\n")
        if usr_choice.isnumeric():
            curr_length = len(sequence)
            for i in range(curr_length, int(usr_choice) + curr_length):
                sequence.append(sequence[i-2] + sequence[i-1])
            print(sequence)
        elif usr_choice == "seq":
            print(sequence)
        elif usr_choice == "redo":
            get_inp()
        elif usr_choice == "quit":
            quit()
        elif usr_choice == "search":
            which_num = input("do you want to find the element by 'indx' or 'find' a num\n")
            if which_num == "indx":
                indx_chc = input("which element in the array do you want?\n")
                while indx_chc.isnumeric() == False:
                    indx_chc = input("that didn't work, which element in the array do you want?\n")
                indx_chc = int(indx_chc)
                try:
                    print("the {0}{1} element is {2}".format
                          (indx_chc, suffix_grabber(indx_chc), sequence[indx_chc -1]))
                except IndexError:
                    print("that index is not in the sequence\n")
                    continue
            elif which_num == "find":
                num_to_look_for = input("which number do you want to find?\n")
                if num_to_look_for.isnumeric():
                    num_to_look_for = int(num_to_look_for)
                    find_num(num_to_look_for)
                else:
                    print("that doesnt work")
                    continue
            else:
                continue

def get_inp():
    global sequence
    sequence = []
    while True:
        first_num = input("what do you want the first number in the sequence to be?")
        if first_num.isnumeric():
            sequence.append(int(first_num))
            break
        else:
            print("that doesn't work, try again")

    while True:
        second_num = input("what do you want the second number in the sequence to be?\n")
        if second_num.isnumeric():
            sequence.append(int(second_num))
            break
        else:
            print("that doesn't work, try again")
    ground_control()


get_inp()
