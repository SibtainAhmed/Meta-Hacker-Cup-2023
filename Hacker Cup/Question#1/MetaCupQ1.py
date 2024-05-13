# file = open('Question#2\cheeseburger_corollary_2_validation_input')

def solve():
    S, D, K = map(int, file.readline().strip().split(' '))
    if K+1<=(S*2+D*2) and K<=(S+D*2):
        return 'YES'
    else:
        return 'NO'


noOfTestCases = int(file.readline())


with open ('SolOfQ1.txt', 'w+') as file2:  
    for i in range(1, noOfTestCases+1):
        file2.write(f"Case #{i}: {solve()}\n") 


file.close()