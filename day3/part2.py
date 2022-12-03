import string
if __name__ == "__main__":

    lowercase = list(string.ascii_lowercase.strip())
    uppercase = list(string.ascii_uppercase.strip())

    total = 0
    print("Hello")
    with open("input.txt") as f:
        content = f.readlines()
        num_groups = int(len(content) / 3)
        for i in range(num_groups):
            start_index = i*3
            first_elf = list(content[start_index])
            second_elf = list(content[start_index+1])
            third_elf = list(content[start_index+2])
            
            unique_first_elf = set(first_elf)

            for j in unique_first_elf:
                if (j in second_elf) and (j in third_elf):
                        if (j in lowercase):
                            index = lowercase.index(j)
                            total += (index+1)
                        elif (j in uppercase):
                            index = uppercase.index(j)
                            total += (27 + index)
    
    print(total)
