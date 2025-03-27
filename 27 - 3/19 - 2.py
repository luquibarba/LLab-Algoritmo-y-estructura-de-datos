while True: 
    a = int(input("Que edad tiene??"))
    if a < 3:
        print ("Su entrada es gratis")
    elif a > 3 and a < 12:
        print("Su entrada sale 10$")
    elif a < 12:
        print("Su entrada sale 15$") 