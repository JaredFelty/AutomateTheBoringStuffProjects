print('Enter a number:')
num = input()
try:
    num = int(num)
except:
        print('That is not a number. Try again:')
        num = input()
        num = int(num)
        

def collatz(number):
        if number % 2 == 0:
         number = number//2
        elif number % 2 == 1:
         number = 3* number + 1
        print(number)
        return number

print(num)
while num != 1:
    num = collatz(num)

    