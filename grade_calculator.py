#user input our marks and calculate grade


math_marks = int(input("Enter your math marks: "))
physics_marks = int(input("Enter your physics marks: "))

inquluded_marks = math_marks + physics_marks
if (inquluded_marks >= 180):
    print("grade A")
elif (inquluded_marks >= 160):
    print("grade B")
elif (inquluded_marks >= 140):
    print("grade C")
elif (inquluded_marks >= 120):
    print("grade D")
else:  
    print("grade F")
