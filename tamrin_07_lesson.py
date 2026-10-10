lesson_list=[]

while True:
    print("1)Add Lesson")
    print("2)Print Lesson List")
    print("3)Sum Lesson")
    print("0)Exit")

    choice = int(input("Choice: "))
    print("_____________________________________")

    match choice:
        case 1:
            print("Enter Lesson Information")
            title = input("Enter Title: ")
            teacher = input("Enter Teacher: ")
            code=int(input("Enter Code: "))
            unit=int(input("Enter Unit: "))

            lesson={
                "title":title,
                "teacher":teacher,
                "code":code,
                "unit":unit
            }
            sum_unit=0
            for course in lesson_list:
                sum_unit += course["unit"]
            if unit in [1,2,3,5] and (sum_unit+unit)<=17:
                lesson_list.append(lesson)
                print("Lesson Added Successfully")
            else :
                print("Invalid")

        case 2:
            print("Lesson List:")
            print("[")
            for lesson in lesson_list:
                print(lesson)
            print("]")

        case 3:
            print("Sum of units:")
            sum_unit=0
            for lesson in lesson_list:
               sum_unit += lesson["unit"]
            print(sum_unit)

        case 0:
            print("Exit")
            break

        case _:
            print("Invalid Option")

    print("_____________________________________")