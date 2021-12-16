
def grades(m):

    if m<=100 and m>=0:
        remainder = m % 5
        determiner = m % 10

        if m >= 38:
            if determiner == 5 or determiner == 0:
                return print("The marks stayed  " + str(m))
            elif determiner > 5:
                if remainder >= 3:
                    p = (m - determiner) + 10
                    return print("Marks rounded to " + str(p) + " the marks before rounding was " + str(m))
                else:
                    return print("Marks didn't change it is still " + str(m))
            elif determiner < 5:
                if remainder >= 3:
                    p = m - determiner
                    return print(
                        "Marks rounded to " + str(p + 5) + " the marks before rounding was " + str(m))
                else:
                    return print("Marks didn't change it is still " + str(m))
        else:
            return print("The student Failed with " + str(m) + " Marks")

    else:
        return print("The marks: "+str(m)+" is not in the range of 0 and 100")


n=int(input("what are number of students: "))
p=0

marks = []


if n<= 60 and n>0 :
    marks = []
    while p < n:
        marks_imput = int(input("input the marks: "))
        marks.append(marks_imput)
        p += 1
    for x in marks:
        grades(x)
else:
    print("Number of students should be between 0 and 60")
