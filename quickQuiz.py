


# Download
# Copy and paste into python in terminal

def game():
    x=0
    recycle = ["recycling bin", "recycle", "Recycling bin", "Recycle", "Recycle Bin", "recycling"]
    trash= ["trash", "trash bin", "Trash", "Trash bin", "Trash Bin", "trash bin"]
    compost=["Compost bin", "Compost", "compost","Compost Bin", "compost bin", "composting"]
    for i in range(3):
        guess = input("In which bin do you put toothpaste tubes in?     ")
        if guess in trash:
            print("Correct!")
            x=x+1
            break
        else:
            print("Try Again!")
    for j in range (3):
        guess2= input("In which bin do you put tea bags in?     ")
        if guess2 in compost:
            print("Correct!")
            x=x+1
            break
        else:
            print("Try Again!")
    for k in range (3):
        guess3= input("In which bin do you put strawberries in?     ")
        if guess3 in compost:
            print("Correct!")
            x=x+1
            break
        else:
            print("Try Again!")
    for l in range (3):
        guess4= input("In which bin do you put plastic take out containers in?     ")
        if guess4 in recycle:
            print("Correct!")
            x=x+1
            break
        else:
            print("Try Again!")
    for m in range (3):
        guess5= input("In which bin do you put paper take out containers in?     ")
        if guess5 in trash:
            print("Correct!")
            x=x+1
            break
        else:
            print("Try Again!")
    print("You got", x, "right!")

game()
