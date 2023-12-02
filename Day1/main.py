# Task 2
def clearAlpha(line):
    numeric = []
    for char in line:
        if '0' <= char <= '9':
            numeric.append(char)
    return numeric

def Day1TaskOne():
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")    
        filtered = list(map(clearAlpha, lines))
        cleared = list(filter(lambda list: len(list) > 0, filtered))
        sums = list(map(lambda values: int(values[0] + values[-1]), cleared))
        totalSum = sum(sums)
        print(totalSum)

# Task Two
def getNumbers(line):
    idx = 0
    numbers = []
    print(line)
    while idx < len(line):
        current = line[idx]
        if '0' <= current <= '9':
            numbers.append(current)
        else:
            for number, phrase, offset in [("1", "one", 3), ("2", "two", 3), ("3", "three", 5), ("4", "four", 4), ("5", "five", 4), ("6", "six", 3), ("7", "seven", 5), ("8", "eight", 5), ("9", "nine", 4)]:
                if(foundNumber(line[idx: idx + offset], phrase)):
                    numbers.append(number)
                    #idx = idx + offset
        idx = idx + 1
    return numbers
        
def foundNumber(fragment, seeking):
    if len(fragment) < len(seeking):
        return False
    for idx in range(0, len(seeking)):
        if fragment[idx] != seeking[idx]:
            return False
    return True

def Day1TaskTwo():
    with open("input.txt", "r") as s:
        sample = s.read().split("\n")
        filtered = list(map(getNumbers, sample))
        cleared = list(filter(lambda x: len(x) > 0, filtered))
        sums = list(map(lambda values: int(values[0] + values[-1]), cleared))
        total = sum(sums)
        print(total)

Day1TaskOne()
Day1TaskTwo()
