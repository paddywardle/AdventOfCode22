if __name__ == "__main__":

    total = 0

    with open ("input.txt") as f:
        for line in f.readlines():
            line_list = line.split()
            game_score = 0
            
            if ((line_list[0] == "A" and line_list[1] == "X") | (line_list[0] == "B" and line_list[1] == "Y") | (line_list[0] == "C" and line_list[1] == "Z")):
                total += 3
                if (line_list[1] == "X"):
                    total += 1
                elif (line_list[1] == "Y"):
                    total += 2
                elif (line_list[1] == "Z"):
                    total += 3
            elif ((line_list[0] == "A" and line_list[1] == "Z") | (line_list[0] == "B" and line_list[1] == "X") | (line_list[0] == "C" and line_list[1] == "Y")):
                total += 0
                if (line_list[1] == "X"):
                    total += 1
                elif (line_list[1] == "Y"):
                    total += 2
                elif (line_list[1] == "Z"):
                    total += 3
            elif ((line_list[0] == "A" and line_list[1] == "Y") | (line_list[0] == "B" and line_list[1] == "Z") | (line_list[0] == "C" and line_list[1] == "X")):
                total += 6
                if (line_list[1] == "X"):
                    total += 1
                elif (line_list[1] == "Y"):
                    total += 2
                elif (line_list[1] == "Z"):
                    total += 3
    print(total)