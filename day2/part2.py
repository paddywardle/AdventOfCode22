if __name__ == "__main__":

    total = 0

    with open ("input.txt") as f:
        for line in f.readlines():
            line_list = line.split()
            
            if (line_list[1] == "Y"):
                total += 3
                if (line_list[0] == "A"):
                    total += 1
                elif (line_list[0] == "B"):
                    total += 2
                elif (line_list[0] == "C"):
                    total += 3
            elif (line_list[1] == "X"):
                total += 0
                if (line_list[0] == "B"):
                    total += 1
                elif (line_list[0] == "C"):
                    total += 2
                elif (line_list[0] == "A"):
                    total += 3
            elif (line_list[1] == "Z"):
                total += 6
                if (line_list[0] == "C"):
                    total += 1
                elif (line_list[0] == "A"):
                    total += 2
                elif (line_list[0] == "B"):
                    total += 3
    print(total)