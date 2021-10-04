number = 15
step = 0
n_list = []
n_list.append(number)

#3n+1

while number != 1:

    step = step + 1
    if number % 2 == 0:
        number = number / 2
    else:
        number = number * 3 + 1
    
    number = int(number)

    n_list.append(number)

    print(f'Step {step}\nNumber: {number}\n')
print(f'Total Steps: {step}\nLog: {n_list}\nHighest number: {max(n_list)}')
