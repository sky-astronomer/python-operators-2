print("welcome to my smart school day planner program")
print("Answer this quick questions and I will help plan your day" )
homework=input("do you have homework: ")
sunny=input("Is it sunny outside: ")
rainy=input("Is it rainy outside: ")
Day=input("what day is it today: ").lower()
print()
print(f"&&&&&&Your plan for {Day}&&&&&&&")
print()
if Day in ("saturday", "sunday"):
    print("it is the weekend, enjoy your day")
if Day in ("monday","wednesday","friday"):
    print("Today you have alot of homework, first finish it then rest")
if Day in("tuesday", "thursday"): 
    print("Today you have homework, but not so much, so rest abit and then do homework") 
else:
    print("Day not recognised, check your spellings")
if sunny=="yes" and homework=="no":
    print("Go play outside, you have no homework!")  
if sunny=="yes" and homework=="yes":
    print("first finish your homework. Then go play outside")
if sunny=="yes" or homework=="no":
    print("first finish your homework. Then do not go outside")
if rainy=="yes" and homework=="no":
    print("finish your homework and do not go outside")
print()
print("planner complete! Have a wonderful day")
