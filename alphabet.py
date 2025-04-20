keypad = {
    '1': 'A',
    '2': 'B',
    '3': 'C',
    '4': 'D',
    '5': 'E',
    '6': 'F',
    '7': 'G',
    '8': 'H',
    '9': 'I',
    '0': 'J'
}

text = ""

while True:
    key = input("Press a number(0-9), or 'q' to QUIT")

    if key == 'q':
        break
    elif key in keypad:
        text += keypad[key]
        print("Current text:", text)
    else:
        print("Invalid input.")

print("Final text:", text)