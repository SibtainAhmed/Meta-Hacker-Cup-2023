file = open('Question#2\cheeseburger_corollary_2_input.txt')

def solve():
    a, b, c = map(int, file.readline().strip().split(' '))
    if c<a and c<b:
        return 0
    elif 1/a >= 2/b:
        s = c//a
        # not added extra condition for double burger
        return s
    else:
        d = c//b
        s = (c-d*b)//a
        return (d*2)+s if s else (d*2)-1


noOfTestCases = int(file.readline())


with open ('Question#2\ActualSolOfQ2.txt', 'w+') as file2:  
    for i in range(1, noOfTestCases+1):
        file2.write(f"Case #{i}: {solve()}\n") 


file.close()


# print(solve())