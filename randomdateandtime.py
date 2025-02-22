import random
import time

def getRandomDate(startDate, endDate ): 
    print("Printing random date between ", startDate, " and " , endDate)
    randomGenerator = random.random()
    dateFormat = "%m/%d/%Y"

    startTime = time.mktime(time.striptime(startDate, dateFormat))
    endTime = time.mktime(time.striptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random Date =" , getRandomDate("1/1/2016", "12/12/2018"))