# external imports
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# internal imports
from classification import createExerciseDict, generateFeatureVector


__all__ = ["randomForestClassification"]


# trains a model based on the user's @code {featureSets} & @code {labels} and returns a new exercise routine based on that model
def randomForestClassification (featureSets, labels, masterDict) : 

    # split data for cross validation
    x_train, x_test, y_train, y_test = train_test_split(featureSets, labels, test_size=0.2, random_state=0)

    # train random forest classifier
    classifier = RandomForestClassifier(n_estimators=10)
    classifier = classifier.fit(x_train, y_train)

    # determine model accuracy
    y_predict = classifier.predict(x_test)
    print('\nRandom Forest Accuracy: ' + str(accuracy_score(y_test, y_predict)*100) + '%')

    # generate new exercise plans until one predicted to be liked is found
    newExercises = []
    like_prediction = 0
    while like_prediction == 0:
        newExercises = generateFeatureVector(masterDict)
        like_prediction = classifier.predict([newExercises])

    # replace encoding with names of exercises
    exerciseNames = []
    for exercise in newExercises:
        exerciseNames.append(masterDict[exercise]['name'])

    return exerciseNames