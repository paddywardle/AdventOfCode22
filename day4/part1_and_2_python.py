if __name__ == "__main__":
    total_part1 = 0
    total_part2 = 0
    num_lines = 0
    overlap = 0
    with open("input.txt") as f:
        
        for line in f.readlines():
            a, b = line.split(',')
            a_1, a_2 = a.split('-')
            b_1, b_2 = b.split('-')
            num_lines += 1

            if ((int(a_1) <= int(b_1)) and (int(a_2) >= int (b_2))) or ((int(a_1) >= int(b_1)) and (int(a_2) <= int (b_2))):
                total_part1 += 1

            if ((int(a_1) <= int(b_1)) and (int(a_2) >= int (b_2))) or ((int(a_1) >= int(b_1)) and (int(a_2) <= int (b_2))) or ((int(a_2) >= int (b_1)) and (int(a_1) < int(b_1))) or ((int(b_2) >= int (a_1)) and (int(b_1) < int(a_1))):
                total_part2 += 1
        
    print(total_part1)
    print(total_part2)