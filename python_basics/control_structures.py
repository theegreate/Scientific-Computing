#ask user for integer input and checks if odd or even
user_input=int(input("Enter integer:"))
#check if odd or even
def check_integer(user_input):
    if user_input%2 == 0:
      print(f"{user_input} is even")

    else:
      print(f"{user_input} is odd")

#call the function
check_integer(user_input)



#for loop to list even numbers from 1 to 50
print(f"for loop to list even numbers from 1 to 50")
for i in range(1,50):
    if i % 2 == 0:
        print(i)

#while loop to print numbers from 10 in reverse order
print(f"while loop to print numbers from 10 in reverse order")
i=10;
while i>=1:
    print(i)
    i-=1





