#!python3
# Write a program that uses a for loop to ask the user to enter
# in 5 numbers.  The program will determine the sum of the 5 numbers
# and calculate the average
# You must use only 1 input statement in your program
y=0
for i in range(0, 5):
    x = int(input("Enter a number: "))
    y = y+x
    avg = y/5
print(f"The sum of the number is {y}, the average of these number is {avg}")