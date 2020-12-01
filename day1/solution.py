input = open('input.txt').read().split('\n')

n = len(input)

# Part 1 Solution
for i in range(n):

    for j in range(i, n):

        if int(input[i]) + int(input[j]) == 2020:
            ans1 = int(input[i]) * int(input[j])
            break

# Part 2 Solution
for i in range(n):

    for j in range(i, n):

        for k in range(j, n):

            if int(input[i]) + int(input[j]) + int(input[k]) == 2020:
                ans2 = int(input[i]) * int(input[j]) * int(input[k])
                break
        
    
print(ans1)
print(ans2)