zeros = set()
potential = set()
neither = set()
everyone = set()
people = {}
mostContacted = {}
virality = {}
spreaders = set()
contacted = set()
spreaderZombie = []
regularZombies = []

def zombiePred():
    pass

def regularZombie(people, person, regularZombies):
    for i in people[person]:
        if i not in neither or i not in potential:
            return ""
    
    print(f"{people[person]} {person}")
    
    if len(regularZombies) < 1:
        regularZombies.append(person)
        return f"{person}"
    else:
        spreaderZombie.append(person)
        return f", {person}"

def spreaderZombies(people, person, spreaderZombie):
    for i in people[person]:
        if i not in potential:
            return ""
    if len(spreaderZombie) < 1:
        spreaderZombie.append(person)
        return f"\n\nSpearder Zombies: {person}"
    else:
        spreaderZombie.append(person)
        return f", {person}"

def maximumDistance(potential, person, people, visited):
    if person in potential:
        return 0

    dist = []
    for contact in people[person]:
        dist.append(1 + maximumDistance(potential, contact, people, visited))

    return max(dist)

def patientZero(spreaders):
    for i in spreaders:
        if i not in contacted:
            zeros.add(i)
    return ", ".join(sorted(zeros))

def potentialZombies(contacted):
    for i in contacted:
        if i not in spreaders and i not in potential:
            potential.add(i)
    return ", ".join(sorted(potential))

def neitherZZ(total):
    for i in total:
        if i not in zeros and i not in potential and i not in neither:
            neither.add(i)
    return ", ".join(sorted(neither))

def mostViral(virality):
    highest = max(virality.values())
    mostViral = [key for key, value in virality.items() if value == highest]
    return ", ".join(mostViral)

def highestContacted(mostContacted):
    highest = max(mostContacted.values())
    mostContactedList = [key for key, value in mostContacted.items() if value == highest]
    return ", ".join(mostContactedList)

file = "zombie-input/Dataset1.txt"

with open(file, "r") as r, open("outputy.txt", "w") as f:
    f.write("Contact records:\n")
    for line in r:
        line = line.strip()
        names = line.split(",")

        spreaders.add(names[0])
        contacted.update(names[1:])

        contacts = ", ".join(names[1:])
        f.write(f"  {names[0]} had contact with {contacts}\n")

        people[names[0]] = names[1:]

        virality[names[0]] = len(names[1:])

        for i in names[1:]:
            mostContacted[i] = 1 + mostContacted.get(i, 0)
        for i in names:
            everyone.add(i)

    f.write("\n")

    total = contacted | zeros

    f.write(f"Patient zeros: {patientZero(spreaders)}\n")
    f.write(f"Potential zombies: {potentialZombies(contacted)}\n")
    f.write(f"Neither patient zero nor potential zombie: {neitherZZ(total)}\n")
    f.write(f"Most viral people: {mostViral(virality)}\n")
    f.write(f"Most contacted people: {highestContacted(mostContacted)}\n")
    f.write("\n")
    f.write("Maximum distance from a potential zombie:\n")
    everyone = list(everyone)
    distances = {}
    for person in everyone:
        distances[person] = maximumDistance(potential, person, people, set())
    distances = dict(sorted(distances.items(), key=lambda item: item[1], reverse=True))
    for key, value in distances.items():
        f.write(f"{key}: {value}\n")
    for person in spreaders:
        f.write(f"{spreaderZombies(people, person, spreaderZombie)}")

    f.write("\nRegular Zombies: ")
    for person in people:
        f.write(f"{regularZombie(people, person, regularZombies)}")
    if not regularZombies:
        f.write("None")


