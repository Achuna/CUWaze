walkingSpeed = 4.54667

answer = ""
while True:
    answer = input("Enter distance (ft): ")
    if answer == "q": break
    distance = float(answer)
    print("Time: " + str(distance/walkingSpeed))