#!/usr/bin/env python3

# written by Aditya Singgih for COMP9041 assignment 2
# part of the initial code were developed by andrewt@cse.unsw.edu.au on October 2017
# https://cgi.cse.unsw.edu.au/~cs2041/assignments/UNSWtalk/


import os, shutil, re, datetime
from flask import Flask, render_template, session, request, flash, redirect, url_for, Response
students_dir = "dataset-small";

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp')
def signUp():
    pass


@app.route('/showSignIn')
def showSignIn():
    return render_template('signin.html')


@app.route('/home', methods=['GET','POST'])
def home():
    if 'zID' not in session:
        students = sorted(os.listdir(students_dir))
        studentList = dict()                                                # list of all students in the dataset

        imgHash=dict()

        for student in students:
            filePath=os.path.join(students_dir, student)
            studentList[student]=filePath

        try: 
            zID = request.form.get("inputZID")
            pw = request.form.get("inputPassword")

            dirPath = os.path.join(studentList[zID], "student.txt")
            stuInfo = dict()

            obtainInfo(dirPath, stuInfo)

            storedPass = stuInfo['password'].strip()
            storedID = stuInfo['zid'].strip()


            #
            # Authentication shit below
            #

            if zID != storedID or pw != storedPass:
                flash("Wrong username / password supplied")
                return redirect(url_for('showSignIn'))

            try:
                getImage(studentList, storedID, imgHash)                    # Add a profile image

            except Exception as e:
                print(str(e))

            # End authentication shit

            friendsList=stuInfo['friends'][2:len(stuInfo['friends'])-1].split(', ')

            for friend in friendsList:
                getImage(studentList, friend, imgHash)

            session['dataDirectory'] = studentList[zID]


            friendsInfo = getFriends(imgHash, studentList)
            session['friendsList']=friendsInfo

            posts = dividePCR(session, 'dataDirectory')
            pcr = hashPCR(posts, session, 'dataDirectory')


            for posts in pcr.values():
                for item in posts:
                    postOwner = item['from'].strip()
                    if postOwner not in imgHash:
                        getImage(studentList, postOwner, imgHash)

            
            complete = getFriends(imgHash, studentList)
            

            session['zID'] = zID
            session['imgInfo'] = imgHash
            profName = stuInfo['full_name']
            session['stuInfo'] = stuInfo
            session['studentInfo'] = studentList
            session['allInvolved'] = complete
            session['ListOfFriends'] = friendsList

            # print(len(session))
            return render_template('home.html', profName=profName.split()[0],
                                                pcr=pcr,
                                                friendsInfo=friendsInfo,
                                                imgHash=imgHash,
                                                complete=complete,
                                                ownerID=stuInfo['zid'].strip()
                                                )

        except Exception as e:
            flash("Our server encountered an error")

            return redirect(url_for('showSignIn'))

    else:

        complete = session.get('allInvolved', None)
        imgHash = session.get('imgInfo', None)
        pcr = session.get('PCR', None)
        stuInfo = session.get('stuInfo', None)
        friendsInfo=session.get('friendsInfo',None)
        profName = stuInfo['full_name']

        posts = dividePCR(session, 'dataDirectory')
        pcr = hashPCR(posts, session, 'dataDirectory')

        # for i in posts.values():
        #     print(i)

        for posts in pcr.values():
            for item in posts:
                postOwner = item['from'].strip()
                if postOwner not in imgHash:
                    getImage(studentList, postOwner, imgHash)

        return render_template('home.html', profName=profName.split()[0],
                                            pcr=pcr,
                                            friendsInfo=friendsInfo,
                                            imgHash=imgHash,
                                            complete=complete,
                                            ownerID=stuInfo['zid'].strip()
                                            )


@app.route('/myProfile', methods=['GET', 'POST'])
def myProfile():
    if 'zID' not in session:
        flash("You need to be logged in to do that")
        return render_template('signin.html')

    stuInfo = session.get('stuInfo', None)
    imgHash = session.get('imgInfo', None)

    profName=stuInfo['full_name']
    profImg=imgHash[session.get('zID', None)]
    # print(profImg)
    return render_template('profile.html', stuInfo=stuInfo, 
                                            profName=profName,
                                            profImg=profImg
                                            )


@app.route('/friends', methods=['GET', 'POST'])
def friends():
    # print(len(session))
    if 'zID' not in session:
        flash("You need to be logged in to do that")
        return render_template('signin.html')

    studentsInfo = session.get('studentInfo', None)
    stuInfo = session.get('stuInfo', None)
    imgHash = session.get('imgInfo', None)
    profName=stuInfo['full_name']
    friendsInfo=session.get('friendsList', None)
    listOfFriends = session.get('ListOfFriends', None)

    return render_template('friendsList.html', profName=profName.split()[0],
                                                imgHash=imgHash,
                                                friendsInfo=friendsInfo,
                                                zID=stuInfo['zid'].strip(),
                                                stuInfo=stuInfo,
                                                listOfFriends=listOfFriends
                                                )


@app.route('/friends/<friendsZID>', methods=['GET', 'POST'])
def showProfile(friendsZID):
    if 'zID' not in session:
        flash("You need to be logged in to do that")
        return render_template('signin.html')

    thisFriendInfo=session.get('friendsList', None)[friendsZID]
    imgHash = session.get('imgInfo', None)
    
    profName=thisFriendInfo['full_name']
    fName=profName.split()[0]
    profImg=imgHash[friendsZID]


    studentList = session.get('studentInfo')
    dataDirectory = studentList[friendsZID]
    session['friendDataDir'] = dataDirectory

    posts = dividePCR(session, 'friendDataDir')
    pcr = hashPCR(posts, session, 'friendDataDir')

    friendImgHash = dict()
    friendImgHash[friendsZID] = imgHash[friendsZID]

    otherfriendsList=thisFriendInfo['friends'][2:len(thisFriendInfo['friends'])-1].split(', ')

    for friendOfFriend in otherfriendsList:
        getImage(studentList, friendOfFriend, friendImgHash)

    for posts in pcr.values():
        for item in posts:
            postOwner = item['from'].strip()
            if postOwner not in friendImgHash:
                getImage(studentList, postOwner, friendImgHash)


    complete = getFriends(friendImgHash, studentList)


    for key in pcr.keys():
        for item in pcr[key]:
            x = item['postID'].split('-')
            postOwner = item['from'].strip()
            # print(postOwner in friendImgHash)
            ownersName = complete[postOwner]['full_name'].strip()

    return render_template('othersProfile.html', stuInfo=thisFriendInfo, 
                                            profName=profName,
                                            fName=fName,
                                            profImg=profImg,
                                            complete=complete,
                                            pcr=pcr,
                                            friendImgHash=friendImgHash
                                            )

@app.route('/writePost/<maxPostID>', methods=['POST'])
def writePost(maxPostID):
    content = request.form.get("post")

    studentList = session['studentInfo']

    if request.referrer.split("/")[-1] == 'home':
        key = session.get('zID')
        retURL = url_for('home')

    else:
        key = request.referrer.split("/")[-1]
        retURL = url_for('showProfile', friendsZID=key)
    
    newPostCount = str(int(maxPostID)+1)

    filePath = os.path.join(studentList[key], newPostCount + ".txt")
    # print(filePath)

    with open (filePath, "w+") as file:
        file.write("from: " + str(session.get('zID')) + "\n")
        file.write("time: " + str(datetime.datetime.now().isoformat()) + "\n")
        file.write("message: " + str(content) +"\n")

    return redirect(retURL)


@app.route('/deletePost/<postID>', methods=['GET'])
def deletePost(postID):
    pass

    studentList = session['studentInfo']

    if request.referrer.split("/")[-1] == 'home':
        key = session.get('zID')
        retURL = url_for('home')

    else:
        key = request.referrer.split("/")[-1]
        retURL = url_for('showProfile', friendsZID=key)

    toBeDel = postID + ".txt"

    filePath = os.path.join(studentList[key], toBeDel)
    os.remove(filePath)

    return redirect(retURL)





@app.route('/logout', methods=['GET','POST'])
def logout():
    session.clear()
    return redirect(url_for('showSignIn'))


def getNonFriendPoster(studentList):
    nonFriendPoster = dict()


def getFriends(imgHash, studentsInfo):
    friendsInfo = dict()
    for student in imgHash:
        # if student != session.get('zID',None):
        path = os.path.join(studentsInfo[student], "student.txt")
        temp = dict()
        friendsInfo[student] = obtainInfo(path, temp)

    return friendsInfo


def obtainInfo(filePath, storage):
    with open(filePath) as file:
        while True:
            details = file.readline()
            if details:
                item = details.split(":")
                key = item[0]
                val = item[1]
                storage[key] = val[:-1]
            else:
                break
    return storage

def dividePCR(ses, dataDirKey):

    dirPath = ses.get(dataDirKey, None)

    test = None
    nope = ["student.txt", "img.jpg"]
    posts = dict()

    previousKey = None
    for item in os.listdir(dirPath):

        if item not in nope:
            temp = item.split("-")

            if len(temp) == 1:
                key = temp[0][0]
            else:
                key = temp[0]

            if key not in posts:
                if previousKey != None and previousKey != key:

                    # '4-10', '4-2', 3
                    # the sort key first sort by the first integer, and then by the second integer, 
                    # and the next one, if exists
                    # sorted output will be '3', '4-2', '4-10'

                    posts[previousKey].sort(key=lambda x: [int(y) for y in x.split('-')])

                posts[key] = []

            load = item.split(".")[0]
          
            posts[key].append(load)

            previousKey = key

    posts[sorted(posts.keys())[-1]].sort(key=lambda x: [int(y) for y in x.split('-')])

    return posts


def hashPCR(pcrStorage, ses, dataDirKey):
    dirPath = ses.get(dataDirKey, None)
    pcrDict = dict()
    for k,v in pcrStorage.items():
        info = []
        for item in v:
            postDetails = dict()
            name = item + ".txt"
            dataPath = os.path.join(dirPath, name)
    
            obtainInfo(dataPath, postDetails)
            postDetails['postID'] = item

            info.append(postDetails)

        if k not in pcrDict:
            pcrDict[k] = info

        else:
            pcrDict[k].update(info)

    return pcrDict

def getImage(storageDict, targetID, toStorage):
    if targetID not in toStorage:
        imgPath = ""
        newImgPath = os.path.join("static/img")
        imgPath = os.path.join(storageDict[targetID], "img.jpg")
        newName = targetID + ".jpg"
        newImgPath = os.path.join(newImgPath, newName)
        shutil.copy(imgPath, newImgPath)
        toStorage[targetID]=newImgPath

    return toStorage

def sortKey(item):
    sumA = 0
    for i in item:
        sumA += ord(i)
    return sumA


def displayProfile(ses):
    friendsInfo=ses.get('friendsList', None)
    imgHash = ses.get('imgInfo', None)

    profName=stuInfo['full_name']
    profImg=imgHash[ses.get('zID', None)]
    # print(profImg)
    return render_template('profile.html', stuInfo=stuInfo, 
                                            profName=profName,
                                            profImg=profImg
                                            )




if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=False, port=9000)



