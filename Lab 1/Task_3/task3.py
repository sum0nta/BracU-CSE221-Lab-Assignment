f = open("input3.txt", "r")
f1 = open("output3.txt", "w")
s = int(f.readline())
id = f.readline().split()
marks = f.readline().split()
id = [int(i) for i in id]
marks = [int(i) for i in marks]

for i in range(len(marks) - 1):
    max_index = i

    for j in range(i + 1, len(marks)):
        if marks[j] > marks[max_index]:
            max_index = j
        elif marks[j] == marks[max_index] and id[j] < id[max_index]:
            max_index = j

    marks[i], marks[max_index] = marks[max_index], marks[i]
    id[i], id[max_index] = id[max_index], id[i]

for i in range(len(id)):
    f1.write(f"ID: {id[i]} Mark: {marks[i]}" + "\n")

f1.close()
f.close()