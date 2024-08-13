## CPF Generation and Validation Script
This script generates a random Brazilian CPF (Cadastro de Pessoas Físicas) and verifies its validity. A CPF is an 11-digit number used for tax purposes in Brazil. The script first generates a random 11-digit number, then calculates the first and second verifier digits according to the official algorithm.

# Process Overview:

1. CPF Generation: A random 11-digit number is generated.
1. First Verifier Digit Calculation: The first nine digits are used to calculate the first verifier digit.
2. Second Verifier Digit Calculation: The first verifier digit is added to the first nine digits, and the resulting ten digits are used to calculate the second verifier digit.
3. CPF Validation: The script checks if the generated CPF matches the expected valid format by comparing it with the calculated verifier digits.
4. If the CPF is valid, the script outputs "Valid CPF!". Otherwise, it outputs "Invalid CPF!".

This script provides a simple demonstration of how the CPF verification process works in Python.

