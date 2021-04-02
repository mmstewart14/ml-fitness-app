# external imports
import csv
import random

__all__ = ["createExerciseDict", "generateFeatureVector", "getUserLabels"]

# generates a dictionary from all exercises in master.csv
def createExerciseDict ():
    masterDict = {}

    with open('static/data/master.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        # add dictionary entry of exercise name: muscle group
        for row in csv_reader:
            masterDict[row[0]] = {'name': row[1], 'focus': row[2]}

    return masterDict

# creates a random feature vector with the passed @code {focusDict}
def generateFeatureVector (masterDict):

    featureVector = []
    exerciseOrder = ['quads','hamstrings','back','chest','arms']

    for movementType in exerciseOrder:
        
        # generate list of possible exercise candidates for each exercise in exerciseOrder
        exerciseCandidates = []
        for key, value in masterDict.items():
            
            if  value['focus'] == movementType:
                exerciseCandidates.append(key)

        # select random exercise from list of possible candidates
        featureVector.append(exerciseCandidates[random.randrange(len(exerciseCandidates))])

    return featureVector

# get user feedback on feature vectors to create classifier
def getUserLabels(numDataPoints):

    featureVectors = []
    labels = []
    
    masterDict = createExerciseDict()
    yesCount = 0
    noCount = 0

    print("To better understand your preferences, please indicate which of the following exercise plans you like.")
    
    # show user feature vectors until they have selected 3 that they like and 3 that they don't
    i = 1
    while yesCount < numDataPoints or noCount < numDataPoints:
        
        print("\n--- Plan " + str(i) + " ---")
        
        featureVector = generateFeatureVector(masterDict)
        for exercise in featureVector:
            print(masterDict[exercise]['name'])

        print("--- Do you like Plan " + str(i) + "? (y/n)")
        answer = str(input()).lower()

        answerAcceptable = False
        while not answerAcceptable:
            if answer == 'y':
                answerAcceptable = True
                yesCount += 1
                labels.append(1)
            elif answer =='n':
                answerAcceptable = True
                noCount += 1
                labels.append(0)
            else:
                print("I did not understand your input! Do you like Plan " + str(i) + "? (y/n)")
                answer = str(input()).lower()

        featureVectors.append(featureVector)
        i += 1

    return featureVectors, labels
