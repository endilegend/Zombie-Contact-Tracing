######################################
# Endi Troqe
# 12-09-2024
# Program 5
######################################

#The olny sorting algorithm I used was pythons deafult sort algorithm (Timesort: combination of merge and insertion sort. It is stable) 
# because it has O(nlogn) time complexity (worst case). It is well suited for large data set and simple sorting.

#I used hashsets because I manily used them to check if something is in the set and that is going to be O(1), they also 
#offer O(1) inertion. Worst case scenario could be O(n) but this is rare due to pythons implemation of hash functions.
zeros = set()
potential = set()
neither = set()
everyone = set()
spreaders = set()
contacted = set()

# I used hashmaps becuase it offers o(1) insertion, O(1) lookup for the value of the keys and it offers relitivley solid 
# search for the values with O(n). Worst case scenario could be O(n) but this is rare due to pythons implemation of hash functions.
# Retriving all values or keys is O(n).
people = {}
mostContacted = {}
virality = {}

#needed to be able to insert things quickly (which is O(1) if you insert at the end)
# and also check if the list is empty or not which would be O(1) complexity.
spreaderZombie = []
regularZombies = []
zombiePreds = []


def zombiePred(person, spreaders, people):
    #O(n) to go through all the people of the person
    for i in people[person]:
        #O(1) (average case) to check if person in spreaders set
        if i not in spreaders:
            return ""
    #O(1) to check if list is empty
    if not zombiePreds:
        #O(1) to append at the end of the list
        zombiePreds.append(person)
        return person
    else:
        return f", {person}"
            

def regularZombie(people, person, regularZombies):
    s = False
    p = False
    #O(n) time complexity to go through the values of person
    for i in people[person]:
        #O(1)(average case) to check if person in the set
        if i in spreaders:
            s = True
        #O(1) to check if person in the set
        if i in potential:
            p = True
    #if the contacts are not in spreaders or in potential zombies than the person is not a regular zombie
    if not s or not p:
        return ""
    
    #O(1) to check if the list is empty
    if not regularZombies:
        #O(1) to append to end of list
        regularZombies.append(person)
        return f"{person}"
    else:
        #O(1) to append to end of list
        spreaderZombie.append(person)
        return f", {person}"

def spreaderZombies(people, person, spreaderZombie):
    #O(n) time complexity to go through the values of person
    for i in people[person]:
        #O(1) (average case) to check if person is in potential set
        if i not in potential:
            return ""
    if len(spreaderZombie) < 1:
        #O(1) to insert (average case)
        spreaderZombie.append(person)
        return f"\n Spearder Zombies: {person}"
    else:
        #O(1) to insert
        spreaderZombie.append(person)
        return f", {person}"

def maximumDistance(potential, person, people):
    #O(1) time complexity to check if person is in set (average case)
    if person in potential:
        return 0

    dist = []
    #O(n) time complexity to go through the values of person
    for contact in people[person]:
        dist.append(1 + maximumDistance(potential, contact, people))

    return max(dist)

def patientZero(spreaders):
    #O(n) to go through every person in the spreaders
    for i in spreaders:
        #O(1) to check if the person is in contacted set (average case)
        if i not in contacted:
            #O(1) to insert
            zeros.add(i)
    #O(nlogn) to sort
    return ", ".join(sorted(zeros))

def potentialZombies(contacted):
    #O(n) to go through every one in contacted
    for i in contacted:
        #O(1) to check if the person is in the sets (average case)
        if i not in spreaders and i not in potential:
            #O(1) insertion
            potential.add(i)
    #O(nlogn) to sort
    return ", ".join(sorted(potential))

def neitherZZ(total):
    #O(n) to go through everyone
    for i in total:
        #O(1) to check if the person is in the sets (average case)
        if i not in zeros and i not in potential and i not in neither:
            #O(1) insertion
            neither.add(i)
    #O(nlogn) to sort
    return ", ".join(sorted(neither))

def mostViral(virality):
    #O(n) to check the highest number in the values
    highest = max(virality.values())
    #O(n) operation since it is needed to go through the values and check if the value, takes O(1), equals the highest value
    # and makes a list of every person that has the highest virality and adds the person to the list (O(1))
    mostViral = [key for key, value in virality.items() if value == highest]
    return ", ".join(mostViral)

def highestContacted(mostContacted):
    #O(n) to check the highest number in the values
    highest = max(mostContacted.values())

    #O(n) operation since it is needed to go through the values and check if the value, takes O(1) (average case), equals the highest value
    # and makes a list of every person that has the highest contact rate and adds the person to the list (O(1))
    mostContactedList = [key for key, value in mostContacted.items() if value == highest]
    return ", ".join(mostContactedList)

file = "zombie-input/Dataset3.txt"

part1 = []
with open(file, "r") as r, open("output.txt", "w") as f:
    f.write("Contact records:\n")
    #goes through n lines O(n)
    for line in r:

        line = line.strip()

        #O(n) to split the list
        names = line.split(",")

        #O(1) to add the first name to the set of spreaders
        spreaders.add(names[0])

        #O(n) to add the rest of the names to the contacted set
        contacted.update(names[1:])

        contacts = ", ".join(sorted(names[1:]))
        
        #O(1) to append to list
        part1.append(f"  {names[0]} had contact with {contacts}\n")

        #O(n) time complexity because it takes O(1) to access names[0] of the dictionary and to assign the value to the key
        # but it takes O(n) to slice the list.
        people[names[0]] = names[1:]
        virality[names[0]] = len(names[1:])

         #O(n) to update mostContacted since for each contact we do an O(1) average get and insert in hashmap
        for i in names[1:]:
            mostContacted[i] = 1 + mostContacted.get(i, 0)
        
        #O(n) to go through ames set
        for i in names:
            #O(1) avergae case to insert
            everyone.add(i)

    #O(nlogn), O(n) to go through part1 list and O(nlogn) to sort
    for i in sorted(part1):
        f.write(i)

    f.write("\n")

    #merges the sets, O(n)
    total = contacted | zeros

    f.write(f"Patient zeros: {patientZero(spreaders)}\n")
    f.write(f"Potential zombies: {potentialZombies(contacted)}\n")
    f.write(f"Neither patient zero nor potential zombie: {neitherZZ(total)}\n")
    f.write(f"Most viral people: {mostViral(virality)}\n")
    f.write(f"Most contacted people: {highestContacted(mostContacted)}\n")
    f.write("\n")
    f.write("Maximum distance from a potential zombie:\n")
    distances = {}

    #0(n) to go through everyone
    for person in everyone:
        #runs recursive functions for person to get the value (distance)
        distances[person] = (maximumDistance(potential, person, people))
    
    #O(nlogn) time complexity because of the sort function. 
    distances = dict(sorted(distances.items(), key=lambda item: (-item[1], item[0])))
    for key, value in distances.items():
        f.write(f" {key}: {value}\n")

    f.write("\nExtra Info:")
    #0(n) to go through spreaders set
    for person in spreaders:
        f.write(f"{spreaderZombies(people, person, spreaderZombie)}")

    f.write("\n Regular Zombies: ")
    #0(n) to go through everyone
    for person in people:
        f.write(f"{regularZombie(people, person, regularZombies)}")
    #o(1) to check if regularZombies array is empty or not
    if not regularZombies:
        f.write("None")
    f.write("\n Zombie Predators: ")
    #O(n) to go through every person in spreaders
    for person in spreaders:
        f.write(f"{zombiePred(person, spreaders, people)}")
