 
def day5_func(length: int):

    with open("input.txt") as f:
        split_input = list(f.readline().strip())

    for i in range(len(split_input)-length):
        current = split_input[i:i+length]
        unique = set(current)
        
        if len(unique) == length:
            print("index: " + str(i+length))
            break

if __name__ == "__main__":

    day5_func(4)

    day5_func(14)