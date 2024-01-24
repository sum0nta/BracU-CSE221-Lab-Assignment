def calculate(a,b,op):
  a,b = int(a), int(b)
  if op == "+":
    return a + b
  if op == "-":
    return a - b
  if op == "*":
    return a * b
  if op == "/":
    return a / b
f = open("/Users/sumonta/Desktop/LabSection14_22341019_CSE221LabAssignment1_Fall2023/Task_1b/input1b.txt","r")
f1 = open("/Users/sumonta/Desktop/LabSection14_22341019_CSE221LabAssignment1_Fall2023/Task_1b/output1b.txt","w")

s = int(f.readline())
for i in range(s):
  x = f.readline().split()
  result = calculate(x[1],x[3],x[2])
  f1.write(f"The result of {x[1]} {x[2]} {x[3]} is {result}" + "\n")

f1.close()
f.close()