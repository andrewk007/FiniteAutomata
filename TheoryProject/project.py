#clean the debug code

def main():
    file_name = "sample2.txt"
    #file_name = input("Enter file name")
    calculate(file_name)

def calculate(file_name):
    file = open(file_name)
    content = file.readlines()
    num_states = content[0]
    final_states = tuple(map(int,content[-1].replace(" "," ").rstrip().split(' ')))
    print(final_states)
    keepPlaying = True
    print("Number of states: " + num_states)
    size_alphabet = content[1]
    print("\nSize of alphabet: "+ size_alphabet)
    chars = content[2]
    print("\nLetters: " + chars)
    arr_states = []
    next_states = []

    for i in range(3,int(num_states)+3):
        next_states.append(content[i].replace(" ","").rstrip())
    for i in range(int(num_states)):
        new_state = State(i)
        if i in final_states:
            new_state.functions(size_alphabet,chars,next_states,True)
        else:
            new_state.functions(size_alphabet,chars,next_states)
        arr_states.append(new_state)
    print("Transition Tables: " + str(next_states))
    while(keepPlaying):
        string = input("Enter a string: \n")
        if string == "STOP":
            keepPlaying = False
            break
        curr_state = arr_states[0]
        for char in string:
            if string == "LAMBDA":
                break
            if char not in chars:
                print("ERROR: "+ str(char))
                keepPlaying = False
                return
            for i in curr_state.input_next_state:
                if char == i[0]:
                    curr_state = arr_states[int(i[1])]
                    print("going to state: " + i[1])
        if curr_state.final_state == True:
            print("YES")
        else:
            print("NO")

class State:
    def __init__(self,number):
        self.state_num = number    

    def functions(self,size_alpha,chars,next_states,final_state = False):
        self.final_state = final_state
        self.size = size_alpha
        self.letters = chars.replace(" ","").rstrip()
        self.input_next_state = []# (input, next state)
        transition_state = next_states[self.state_num] 
        for i in range(len(self.letters)):
            self.input_next_state.append((self.letters[i],transition_state[i]))
        print(self.input_next_state)
main()

