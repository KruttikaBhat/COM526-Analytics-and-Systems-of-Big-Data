import pandas as pd
import numpy as np
import random
import operator
import matplotlib.pyplot as plt

#city object
class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2)) #euclidean distance is used
        return distance


#to get fitness for each route
class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness= 0.0

    def routeDistance(self):
        if self.distance ==0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                fromCity = self.route[i]
                toCity = None
                if i + 1 < len(self.route):
                    toCity = self.route[i + 1]
                else:
                    toCity = self.route[0]
                pathDistance += fromCity.distance(toCity)
            self.distance = pathDistance
        return self.distance

    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness


def initialPopulation(popSize, cityList):
    population = []
    for i in range(0, popSize):
        population.append(random.sample(cityList, len(cityList)))
    return population

#This function will rank the routes in the order of their fitness
def rankRoutes(population):
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFitness()
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)


def selection(popRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()

    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i,3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults

def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool

#ordered crossover method
def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []

    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])

    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child

def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    #first put the top 20 in the next generation
    for i in range(0,eliteSize):
        children.append(matingpool[i])

    #perform roulette wheel selection on the population to get the remaining children
    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children

#swap mutation method
def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))

            city1 = individual[swapped]
            city2 = individual[swapWith]

            individual[swapped] = city2
            individual[swapWith] = city1
    return individual

def mutatePopulation(population, mutationRate):
    mutatedPop = []

    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop

def nextGeneration(currentGen, eliteSize, mutationRate):
    popRanked = rankRoutes(currentGen) #order the routes in terms of fitness
    selectionResults = selection(popRanked, eliteSize) #will return the indices of selected parents
    matingpool = matingPool(currentGen, selectionResults) #will get a list of parents from the indices
    children = breedPopulation(matingpool, eliteSize) #perform crossover
    nextGeneration = mutatePopulation(children, mutationRate) #perform mutation
    return nextGeneration

def geneticAlgorithm(cities, popSize, eliteSize, mutationRate, generations):
    #this will store the best route of each generation
    progress = []
    #initialise the population
    population = initialPopulation(popSize, cities)
    best_distance = 1 / rankRoutes(population)[0][1]
    print("Initial distance: " + str(best_distance))
    progress.append(best_distance)

    #iterate the algorithm for the given number of generations
    for i in range(0, generations):
        population = nextGeneration(population, eliteSize, mutationRate)
        best_distance = 1 / rankRoutes(population)[0][1]
        print("Generation %d : %f" % (i+1,best_distance))
        progress.append(best_distance)

    #plot the best routes of each generation
    plt.figure()
    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()

    bestRouteIndex = rankRoutes(population)[0][0]
    bestRoute = population[bestRouteIndex]
    return bestRoute #returns the best route from the final generation

if __name__=="__main__":

    #view the city points
    all_cities=pd.read_csv("cities.csv")
    ax=all_cities.plot.scatter(x='x',y='y',grid='True')
    ax.set_xticks(np.arange(0,250,20))
    ax.set_yticks(np.arange(0,250,20))
    plt.show()

    #create city objects
    cityList = []
    for i in range(0,20):
        cityList.append(City(x=all_cities.loc[i,'x'], y=all_cities.loc[i,'y']))

    #run GA to get best route
    bestRoute=geneticAlgorithm(cities=cityList, popSize=200, eliteSize=20, mutationRate=0.01, generations=200)

    #plot the best route
    xlist=[]
    ylist=[]
    for i in bestRoute:
        xlist.append(i.x)
        ylist.append(i.y)

    plt.figure()
    plt.plot(xlist,ylist)
    plt.scatter(xlist,ylist)
    plt.grid(axis='both')
    plt.xticks(np.arange(0,250,20))
    plt.yticks(np.arange(0,250,20))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
