
from time import sleep

temperature = int(input("What is the temperature of today? "))
travel_time = "..."
activities = "Surfing, Volleyball, Fishing, Swimming or Sunbathing?"
mountain_activities = "skies or snowboard? "

if 25 < temperature < 35:
    print ("It's " + str(temperature) + "degrees outside, remember to put on sunscreen and drink alot of water \n")
    answer = input ("Do you wish to go to the beach? ")
    if answer == "yes":
        print ("You're going to the beach")
        for i in range(3):
            print(travel_time[i], sep=' ', end=' ', flush=True); sleep(0.5)
        print("You arrived at he beach\n")
        beach_activities = input("What do you wish to do at the beach?")
        print ("You went " + beach_activities + "ing")  #kanskje det er mulig å få python til å bøye verbet?
    else:
        print("You're in the shade with a lemonade")

elif temperature > 35:
    print ("It's " + str(temperature) + " degrees outside, you're probably living on the sun")

elif temperature >= 25:
    print ("It's " + str(temperature) + " degrees outside, it's a nice day")

elif temperature >= 15:
    print ("It's " + str(temperature) + " degrees outside, it's a pretty normal day")

elif temperature > 10:
    print ("It's " + str(temperature) + " degrees outside, you should put on a jacket")

elif temperature <= 10:
    print ("It's " + str(temperature) + " degrees outside, you should put some clothes on it's freezing\n")
    answer = input ("Do you wish to go skiing in the mountain? ")
    if answer == "yes":
        print ("You're going to the mountain")
        for i in range(3):
            print(travel_time[i], sep=' ', end=' ', flush=True); sleep(0.5)
        print ("You arrived at the mountain\n")
        input ("Do you wish to use " + mountain_activities)
        if answer == "skies":
            print("You're going downhill skiing")
        else: 
            print ("You're going downhill snowboarding")
    else:
        print("You're staying inside in the heat with a blanket drinking cocoa")
        
