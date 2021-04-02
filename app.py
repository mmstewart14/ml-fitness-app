# external imports
from flask import Flask, render_template, request, redirect
import json

# internal imports
from classification import getUserLabels, generateFeatureVector, createExerciseDict
from supervised_learning import randomForestClassification

app = Flask(__name__)

# set up username and password for app use
print("Please choose a username: ")
username = str(input()).lower()
print("Please choose a password: ")
password = str(input()).lower()

# initialize needed parameters
masterDict = createExerciseDict()
numDataPoints = 5

# get user labels for designated number of feature vectors
featureVectors, labels = getUserLabels(numDataPoints)


# login page
@app.route('/')
def login():
    return render_template('index.html', username=username, password=password)

# home daily exercise page
@app.route('/home', methods=['GET'])
def home():
    exercises = randomForestClassification(featureVectors, labels, masterDict)
    return render_template('home.html', exercise1=exercises[0], exercise2=exercises[1], exercise3=exercises[2], exercise4=exercises[3], exercise5=exercises[4])

# page for getting user initial exercise preferences
@app.route('/classify')
def classify():
    masterDict = json.dumps(createExerciseDict())
    return render_template('classifier.html', exerciseDict=masterDict)

# recieve user's seen feature vectors and labels
@app.route('/getClassifications', methods=['POST'])
def getClassifications():
    featureVectors = request.json['featureVectors']
    labels = request.json['labels']
    return

# add feature vector and dislike label to existing lists when a user provides negative feedback in app
@app.route('/addFeatureVector', methods=['POST'])
def addFeatureVector():
    if request.method == "POST":
        exercises = request.json['exercises']
        featureVector = []
        for exercise in exercises:
            for key, value in masterDict.items():
                if value['name'] == exercise:
                    featureVector.append(key)
        featureVectors.append(featureVector)
        labels.append(0)
    return redirect('/home')