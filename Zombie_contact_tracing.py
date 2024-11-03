
zeros = []
potential = []
neither = []
everyone = set()

virality = {}
spreaders = []
contacted = []


distances = {}
distanceOne = []


def maximumDistance(everyone, zeros, distanceOne):
    if len(everyone) == 0:
        return ""

    z = 99
    
    x = everyone.pop()
    if x in zeros:
        z = 0
    elif x in distanceOne:
        z = 1

    return f"{x}: {z}\n" + maximumDistance(everyone, potential, zeros)


def patientZero(spreaders):
    for i in spreaders:
        if i not in contacted:
            zeros.append(i)

    return  ", ".join(zeros)

def potentialZombies(contacted):
    for i in contacted:
        if i not in spreaders and i not in potential:
            potential.append(i)
            for key, value in distances.items():
                if i in value:
                    distanceOne.append(key)
        
    return ", ".join(potential)

def neitherZZ(total):
    for i in total:
        if i not in zeros and i not in potential and i not in neither:
            neither.append(i)
    return ", ".join(neither)

def mostViral(virality):
    highest = max(virality.values())
    mostViral = [key for key, value in virality.items() if value == highest]
    return ", ".join(mostViral)

def highestContacted(mostContacted):
    highest = max(mostContacted.values())
    mostContacted = [key for key, value in mostContacted.items() if value == highest]
    return ", ".join(mostContacted)


    


file = "Dataset1.txt"



mostContacted = {}
with open(file, "r") as r, open("outputy.txt", "a") as f:
    f.write("Contact records:\n")
    for line in r:
        viral = []

        line = line.strip()
        names = line.split(",")

        spreaders.append(names[0])
        contacted.extend(names[1:])

        viral.extend(names[1:])

        contacts = ", ".join(names[1:])
        f.write(f"  {names[0]} had contact with {contacts}\n")

        distances[names[0]] = names[1:]


        virality[names[0]] = len(viral)

        for i in names[1:]:
            mostContacted[i] = 1 + mostContacted.get(i, 0)  
        for i in names:
            everyone.add(i)
      

    f.write("\n")




    total = set(contacted + zeros)

    f.write(f"Patient zeros: {patientZero(spreaders)}\n")
    f.write(f"Potential zombies: {potentialZombies(contacted)}\n")
    f.write(f"Neither patient zero nor potential zombie: {neitherZZ(total)}\n")
    f.write(f"Most viral people: {mostViral(virality)}\n")
    f.write(f"Most contacted people: {highestContacted(mostContacted)}\n")
    f.write("\n")
    f.write("Maximum distance from a potential zombie:\n")
    f.write(maximumDistance(everyone, zeros, distanceOne))



