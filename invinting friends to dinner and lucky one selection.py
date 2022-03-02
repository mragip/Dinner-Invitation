import random

print("Enter the number of friends joining (including you):")
number = int(input())
friends = {}
if number <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for names in range(1,number + 1):
        names = input()
        friends[names] = 0
    print("")
    print("Enter the total bill value:")
    bill_value =int(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_no = input()

    if lucky_no == "No":
        
        bill_share = round(((bill_value) / number), 2)

        friends_value = dict.fromkeys(friends,(bill_share))
        print("No one is going to be lucky")
        print(friends_value)        
    else:
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")
        
        bill_share = round(((bill_value) / (number - 1)), 2)

        del friends[lucky_one]
        friends_value = dict.fromkeys(friends,(bill_share))
        friends_value[lucky_one] = 0
        print(friends_value)
        

        
        
        





    
    
