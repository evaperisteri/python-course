choice = 'q'

if choice == 'q' or choice == "Q":
    print("Quit")
else:
    print("Continue")

if choice.upper() == "Q":
    print("Quit")
else:
    print("Continue")

#more pythonian
if choice in ('q', 'Q'):
    print("Quit")
else:
    print("Continue")