userReply = input("Do you need to ship a package? (Enter yes or no)")
if userReply == "yes":
    print("we can help you ship that package!")
else:
    print("Please come back when to ship a package. Thank you.")
    
userReply = input("Would you like to buy stamps, buy an envope,or make a copy? (Enter stamps, envope, or copy)")
if userReply == "Stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
     print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
    
    
    