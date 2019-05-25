my_friends = {"2017": ["Bob", "Jack", "Joe", "Jemmy"],
              "2018" : ["Sheena", "Sean", "Lili"] }

print(my_friends)

name = input("Enter a name of your friends list:").strip()

found = False
for key in my_friends:
    if name in my_friends[key]:
        print("You met", name, "in", key, "!")
        found = True
if not found:
    print("You have no friend with name", name)

newName = input("Please enter a new name for a friend:").strip().title()
year = input("Please enter a year for your friend:")

if year in my_friends:
    print("The new friend was added to ", year, "friend list")
    my_friends[year].append(newName)
else:
    print("A new key-value was created for", year)
    my_friends[year] = [newName]

print(my_friends)
