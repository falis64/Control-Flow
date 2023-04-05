#Make a loop with a range that says hello 10 times
#Create another loop with a range that asks for names and appends to list_names
#Make a loop that iterates over each name in list_name and format's it into lowercase in a new variable called list_names_lower
#Make a list of numbers, iterate over the list of values to find if the are even

#1 Make a loop with a range that says hello 10 times
for i in range(2 * 5):
     print("Hello")

# Loop with a range that asks for names and appends to list_names

list_names = []

repeat = range(2)

for i in repeat:
    new_name = input("What is your name?\n")
    list_names.append((new_name))

print(list_names)


# Make a loop that iterates over each name in list_name and format's it into lowercase in a new variable called list_names_lower

list_names_lower = []

for names in list_names:
    names_lower = names.lower()
    list_names_lower.append(names_lower)

print(list_names_lower)

# Iterate over a list of values to find out they are even

num_list = [1, 2, 3, 4, 5, 6, 7, 8]
for num in num_list:
      if num % 2 ==0:
          print("Even number")
      else:
          print("Odd number")

