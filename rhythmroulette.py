import random

def spin_row():
    items = ["#", "E", "&", "A", "#E", "E&", "&A", 
             "#A", "#&", "EA", "#E&", "#EA", "#&A",
             "E&A", "#E&A", "NA"]
    
    patterns = [random.choice(items) for _ in range(4)]

    for index, pattern in enumerate(patterns):
        charFound = pattern.find("#")
        if charFound != -1:
            currentStr = list(pattern)
            currentStr[charFound] = str(index + 1)
            res = ''.join(currentStr)
            patterns[index] = res

    return patterns

def print_row(row):
    print("********************")
    print(" ", (row))
    print("********************")

def main():
    respin = True
    while respin:
        row = spin_row()
        print("Randomizing your new rhythm")
        print_row(row)

        selection = input ("Would you like to spin again? (Y/N): ").upper()

        if selection != 'Y':
            respin = False
            break

if __name__ == '__main__':
    main()