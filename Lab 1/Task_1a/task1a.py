f = open("/Users/sumonta/Desktop/LabSection14_22341019_CSE221LabAssignment1_Fall2023/Task_1a/input1a.txt","r")
f1 = open("/Users/sumonta/Desktop/LabSection14_22341019_CSE221LabAssignment1_Fall2023/Task_1a/output1a.txt","w")

s = int(f.readline())
for i in range(s):
  x = int(f.readline())
  if x % 2 == 0:
    f1.write(f"{x} is an Even number"+"\n")
  else:
    f1.write(f"{x} is an Odd number"+"\n")
f1.close()
f.close()