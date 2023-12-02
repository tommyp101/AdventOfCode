file = open("day1_input.txt", "r")
res = 0
for line in file.readlines():
    line = line.strip()
    leftPtr = 0
    rightPtr = len(line) - 1
    leftDigit = 0
    rightDigit = 0
    for i in range(len(line)):
        if line[i].isdigit():
            leftPtr = i
            leftDigit = line[i]
            break
    for i in range(rightPtr, leftPtr-1, -1):
        if line[i].isdigit():
            rightPtr = i
            rightDigit = line[i]
            break
    two_digit_number = int(leftDigit + rightDigit)
    res += two_digit_number
file.close()
print(res)