import requests
if __name__ == "__main__":

    current = 0
    calories = []
    with open("input.txt") as f:
        
        for line in f.readlines():
            if line.strip() == "":
                calories.append(current)
                current = 0
                continue
            current += int(line)

    calories.sort(reverse=True)
    
    print("Highest calories: " + str(max(calories)))

    print("Top three calorie totals: " + str(calories[0]) + ", " + str(calories[1]) + ", " + str(calories[2]))

    print("Top three calorie totals: " + str(sum(calories[0:3])))