n = float(input("enter the marks: "))
attendance = float(input("enter the attendance: "))
passedmarks = 33
attendance_req = 75
if n>= passedmarks and attendance >= attendance_req:
  print("you are eligible for giving the ETE")
else:
  print("not eligible")