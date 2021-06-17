import math
import random
def foo(x, y ,z):
    return x**3 + 24*y**2 + 9*z - 1

def fitness(x,y,z):
    ans = foo(x,y,z)

    if ans == 0:
        return math.inf
    else:
        return abs(1/ans)

solutions = []
for s in range(1000):
    solutions.append( (random.uniform(0, 1000),
                       random.uniform(0, 1000),
                       random.uniform(0, 1000)
                    ))

for i in range(10000):
    rankedSolutions = []
    for solution in solutions:
        rankedSolutions.append( (fitness(solution[0],solution[1],solution[2]),solution) )
    rankedSolutions.sort()
    rankedSolutions.reverse()

    print(f"=== Gen {i} best Solution ===")
    print(rankedSolutions[0])
    if rankedSolutions[0][0] > 999:
        break
    bestSolutions = rankedSolutions[:100]

    elements = [[],[],[]]
    for s in bestSolutions:
        elements[0].append(s[1][0])
        elements[1].append(s[1][1])
        elements[2].append(s[1][2])
    newGen = []
    for _ in range(1000):
        e1 = random.choice(elements[0]) * random.uniform(0.99,1.01)
        e2 = random.choice(elements[1]) * random.uniform(0.99,1.01)
        e3 = random.choice(elements[2]) * random.uniform(0.99,1.01)

        newGen.append((e1,e2,e3))

    solutions = newGen