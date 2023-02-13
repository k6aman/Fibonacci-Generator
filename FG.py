def  fibonacci(n):

	if n == 1  or n == 0:

		return n;

	else:

		return fibonacci(n-2) + fibonacci(n - 1)
numero = int(input("Enter a positive interger: "))

if numero < 0:
	print("Invalid Number")
i = 0
print("Fibonacci Secession: ")
for i in range(0, numero):
	print(fibonacci(i))