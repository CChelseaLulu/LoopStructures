#q3b
def finalval2():
    x = 8
    while x>+5 and x <=8:
        print(x)
        if x % 2 == 0:
            x = x + 1
        else:
            x = x - 1
    print("Final value", x)

finalval2()

#the loop does not end when the initail value is 7 and 6
#when the initial value is 5, the final value is 5
#when the initial value is 8, the final value is 9
