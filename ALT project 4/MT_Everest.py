#Imports
import Climber as c
import random
import matplotlib.pyplot as plt

#Sets up lists
equipment_list = ["Heavily equipped", "Moderately equipped", "Lightly equipped", "No equipment"]
rations_list = ["Plenty of rations", "Moderate rations", "Low rations", "No rations"]
events_list = ["Nothing", "Blizzard", "Avalanche", "Storm", "Broken foot"]
weather_list = ["Sunny", "Cloudy", "Raining"]

def choose_event():
    roll = random.randint(1, 200)
    if roll <= 5:
        return random.choice(events_list[1:3])  #Blizzard or Avalanche
    elif roll <= 10:
        return random.choice(events_list[3:5])  #Storm or Broken foot
    else:
        return events_list[0]  #Nothing

def base_probability(equipment, rations):
    if equipment == "Heavily equipped":
        if rations == "Plenty of rations":
            return 1.0
        elif rations == "Moderate rations":
            return 0.9
        elif rations == "Low rations":
            return 0.75
        else:
            return 0.40
    elif equipment == "Moderately equipped":
        if rations == "Plenty of rations":
            return 0.90
        elif rations == "Moderate rations":
            return 0.75
        elif rations == "Low rations":
            return 0.4
        else:
            return 0.25
    elif equipment == "Lightly equipped":
        if rations == "Plenty of rations":
            return 0.70
        elif rations == "Moderate rations":
            return 0.55
        elif rations == "Low rations":
            return 0.25
        else:
            return 0.1
    else:  #No equipment
        if rations == "Plenty of rations":
            return 0.40
        elif rations == "Moderate rations":
            return 0.20
        elif rations == "Low rations":
            return 0.05
        else:
            return 0.01

def weather_penalty(weather):
    if weather == "Sunny":
        return 0.00
    elif weather == "Cloudy":
        return -0.05
    else:  #Raining
        return -0.15

def event_penalty(event):
    if event == "Nothing":
        return 0.0
    elif event == "Blizzard":
        return -0.25 #Qauter of probability
    elif event == "Avalanche":
        return -0.40 #2/5 of probability
    elif event == "Storm":
        return -0.20 #Fifth of probability
    else:  #Broken foot
        return -1.00 #No chance of success

def simulate_climbers(n):
    success_count = 0
    failure_count = 0
    successful_climbers = []
    all_climbers = []

    for i in range(n):
        age = random.randint(18, 80)
        equipment = random.choice(equipment_list)
        rations = random.choice(rations_list)
        weather = random.choice(weather_list)
        event = choose_event()

        climber = c.Climber(age, equipment, rations, weather, event)
        all_climbers.append(climber)

        base = base_probability(equipment, rations)
        w_pen = weather_penalty(weather)
        e_pen = event_penalty(event)

        success_prob = base + w_pen + e_pen
      
      #Checks bounds of probability
        if success_prob < 0.0:
            success_prob = 0.0

        if random.random() < success_prob:
            success_count += 1
            successful_climbers.append(climber)
        else:
            failure_count += 1

    return success_count, failure_count, successful_climbers, all_climbers

#Runs simulation and gets results
successes, failures, successful_climbers, all_climbers = simulate_climbers(1000)

print(f"Successful climbs: {successes}, Failed climbs: {failures}")

#Shows info for successful climbers
id = 1
for climber in successful_climbers:
    print(str(id) + ": " + climber.info())
    id = id + 1

#Counts occurrences for each category and makes placeholders (Better for lag)
equipment_counts = [0] * len(equipment_list)
rations_counts = [0] * len(rations_list)
weather_counts = [0] * len(weather_list)
event_counts = [0] * len(events_list)

#Adds each occurence into each category and fills placeholders
for climber in all_climbers:
    #Equipment
    for i in range(len(equipment_list)):
        if climber.equipment == equipment_list[i]:
            equipment_counts[i] = equipment_counts[i] + 1
            break
    #Rations
    for i in range(len(rations_list)):
        if climber.rations == rations_list[i]:
            rations_counts[i] = rations_counts[i] + 1
            break
    #Weather
    for i in range(len(weather_list)):
        if climber.weather == weather_list[i]:
            weather_counts[i] = weather_counts[i] + 1
            break
    #Event
    for i in range(len(events_list)):
        if climber.events == events_list[i]:
            event_counts[i] = event_counts[i] + 1
            break

#Plots 4 bar charts 
plt.figure(figsize=(12, 9))

plt.subplot(2, 2, 1)
plt.bar(equipment_list, equipment_counts, color='C0')
plt.title('Equipment')
plt.ylabel('Number of climbers')
plt.xticks(rotation=25)

plt.subplot(2, 2, 2)
plt.bar(rations_list, rations_counts, color='C1')
plt.title('Rations')
plt.xticks(rotation=25)

plt.subplot(2, 2, 3)
plt.bar(weather_list, weather_counts, color='C2')
plt.title('Weather')
plt.ylabel('Number of climbers')

plt.subplot(2, 2, 4)
plt.bar(events_list, event_counts, color='C3')
plt.title('Events')
plt.xticks(rotation=25)

plt.suptitle(f'Climber conditions (n={len(all_climbers)})')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

#Pie chart to show success vs failure
sizes = [successes, failures]
labels = ['Successful climbers', 'Failed climbers']
plt.figure(figsize=(8,8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title(f"Climbing results (n={successes + failures}) — Successes: {successes}, Failures: {failures}")
plt.axis('equal')

plt.show()