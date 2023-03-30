#-----------
#autoattack
#Aiden Krahn
#Started March 29
#------------

import random

#dictionaries and lists----
x = random.randint(1, 100)
mns = {'taxes':111, 'homework':100 + x, 'studying':20, 'extracurricular':50,
       'botheringmr.white':5, "hidingdeadbodies":100, 'chores':50}


#constants
time = 720
responsibility = 50


#defenitions
def dothething():
    global responsibility
    global time
    while time > 0 or responsibility > 0:
        ssot = list(mns.keys())
        whatone = ssot[random.randint(0, len(ssot)-1)]
        print(f"You remember needing to do {whatone}.")
        doit = input("Take the time for the task?(y/n)  ")
        
        if doit == "n":
            responsibility -= round(mns[whatone] / 14)
            mns.pop(whatone)
            print(f"You didn't spend time on {whatone}.")
            print(f"You have {time} time left, and {responsibility} responsibility left.")
            return responsibility
            
        elif doit == 'y':
            time -= mns[whatone]
            mns.pop(whatone)
            print(f"You spent time on your {whatone}.")
            print(f"You have {time} time left, and {responsibility} responsibility left.")
            return time
        
    if time <= 0:
        print("You ran out of time.")
        
        if responsibility > 10:
            print("You managed to get enough done today.")
            print("You Win.")
            
        elif responsibility <= 10:
            print("You didn't get enough done today.")
            print("You Lose.")
            
    elif responsiblity <= 0:
        print("You are not being responsible.")
        print("You Lose.")
    


#main code
print("You are a human being with *gasp* responsibilities.")
print("Your memory is bad, but you can swear there's task you need to focus on:")
dothething()
