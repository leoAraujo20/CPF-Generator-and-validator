import random

cpf = ''
for i in range(11):
    cpf += str(random.randint(0, 9))
print(cpf)

nineDigits = cpf[0:9]

# verification of the first digit
sumFirstDigit = 0
counter = 10
for i in nineDigits:
    sumFirstDigit += int(i) * counter
    counter -= 1
    
multSumDigits = sumFirstDigit * 10
remainderMultDigits = multSumDigits % 11
firstVerifierDigit = remainderMultDigits if remainderMultDigits <= 9 else 0

# verification of the second digit
tenDigits = nineDigits + str(firstVerifierDigit)

sumSecondDigit = 0
counter = 11
for i in tenDigits:
    sumSecondDigit += int(i) * counter
    counter -= 1

multSumSecondDigit = sumSecondDigit * 10
remainderMultSecondDigit = multSumSecondDigit % 11
secondVerifierDigit = remainderMultSecondDigit if remainderMultSecondDigit <= 9 else 0

# verification of the generated CPF!
finalCpf = tenDigits + str(secondVerifierDigit)
if cpf == finalCpf:
    print('Valid CPF!')
else:
    print('Invalid CPF!')
