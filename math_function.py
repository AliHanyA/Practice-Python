# min
def less(num1,num2):
    if num1 > num2:
        return num2
    elif num1 < num2:
        return num1
    else:
        return 'num1==num2'
# ----------------------------------------------
# max
def big(num1,num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return 'num1==num2'
# -----------------------------------------
# ceil
def ceiling (num):
    return int(num+1)
# -----------------------------------------
#floor
def flooring (num):
    return int(num)
# -----------------------------------------
# abs
def abcluit (num):
    if num<0:
        return num*-1
    else:
        return num
# -----------------------------------------
