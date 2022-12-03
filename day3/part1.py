import string
if __name__ == "__main__":

    lowercase = list(string.ascii_lowercase.strip())
    uppercase = list(string.ascii_uppercase.strip())

    total = 0
    with open("input.txt") as f:

        for line in f.readlines():

            unique = set(line)
            characters = list(line.strip())
            string_length = len(characters)
            halfway = int(string_length/2)

            first_half = characters[0:halfway]
            second_half = characters[halfway:]
            for i in unique:
                if (i in first_half) and (i in second_half):
                    if (i in lowercase):
                        index = lowercase.index(i)
                        total += (index+1)
                    elif (i in uppercase):
                        index = uppercase.index(i)
                        total += (27 + index)
    
    print(total)
