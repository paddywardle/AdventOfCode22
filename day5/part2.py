if __name__ == "__main__":
    
    stack_1 = ['F', 'R', 'W']
    stack_2 = ['P', 'W', 'V', 'D', 'C', 'M', 'H', 'T']
    stack_3 = ['L', 'N', 'Z', 'M', 'P']
    stack_4 = ['R', 'H', 'C', 'J']
    stack_5 = ['B', 'T', 'Q', 'H', 'G', 'P', 'C']
    stack_6 = ['Z', 'F', 'L', 'W', 'C', 'G']
    stack_7 = ['C', 'G', 'J', 'Z', 'Q', 'L', 'V', 'W']
    stack_8 = ['C', 'V', 'T', 'W', 'F', 'R', 'N', 'P']
    stack_9 = ['V', 'S', 'R', 'G', 'H', 'W', 'J']

    stack_list = [stack_1, stack_2, stack_3, stack_4, stack_5, stack_6,
                  stack_7, stack_8, stack_9]

    with open('input.txt') as f:
        for line in f.readlines():
            
            string_list = line.split()
            num_crates = int(string_list[1])
            start_stack_index = int(string_list[3]) - 1
            finish_stack_index = int(string_list[5]) - 1
            starting_stack = stack_list[start_stack_index]

            stack_list[finish_stack_index] = stack_list[start_stack_index][:num_crates] + stack_list[finish_stack_index]

            for i in range(num_crates):
                stack_list[start_stack_index].pop(0)

    final_answer = ''

    for stack in stack_list:
        final_answer += stack[0]

    print(final_answer)
