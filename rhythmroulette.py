import random

def easy_diff():
    return ["#", "&", "#&", "#E&A", "REST"]

def medium_diff():
    return["#", "&", "#&", "#E&", "#EA", "#&A","#E&A", "REST"]

def hard_diff():
    return ["#", "E", "&", "A", "#E", "&A", "#A", "#&", "#E&", "#EA", 
           "#&A","#E&A", "REST"]

def max_diff():
    return ["#", "E", "&", "A", "#E", "E&", "&A", 
             "#A", "#&", "EA", "#E&", "#EA", "#&A",
             "E&A", "#E&A", "REST"]

switcher = {
    1: easy_diff,
    2: medium_diff,
    3: hard_diff,
    4: max_diff
}

def choose_diff(choice):
    return switcher.get(choice, lambda: "unknown")()

def spin_row(diff_level):
    items = diff_level
    
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
    print("", (row))
    print("********************")

def main():
    respin = True

    diff_level = 0

    while True:
        while True:
            user_input = input ("Choose a number for your difficulty level - (1|Easy) (2|Medium) (3|Experienced) (4|Hard): ")
            try:
                diff_level = int(user_input)
                if(diff_level > 0 and diff_level < 5):
                        break
                else:
                    print("Please enter a number between 1 and 4,", f'"{diff_level}" is not an accepted number."')
            except ValueError:
                try:
                    diff_level = float(user_input)
                    if(diff_level > 0 and diff_level < 5):
                        break
                    else:
                        print("Please enter a number between 1 and 4,", f'"{diff_level}" is not an accepted number."')
                except ValueError:
                    print("Please enter a number between 1 and 4,", f'"{user_input}" is not a number.')

        print(f'You have selected difficulty level {diff_level}')

        while respin:
            diff_choice = choose_diff(diff_level)
            row = spin_row(diff_choice)
            print("Randomizing your new rhythm")
            print_row(row)

            selection = input ("Would you like to spin again? (Y/N): ").upper()

            if selection != 'Y':
                respin = False
                break
        
        user_input = input("Would you like to change your difficulty and spin again? (Y/N): ").upper()
        if user_input != 'Y':
            break
        else:
            respin = True

if __name__ == '__main__':
    main()