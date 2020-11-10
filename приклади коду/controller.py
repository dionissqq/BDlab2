from datetime import datetime

class Controller(object):

    def __init__(self, model):
        self.model = model

    def insertPhoto(self, name, description, albumID):
        if (isinstance(name, str) and isinstance(description, str) and isinstance(albumID, int)):
            self.model.insertPhoto(name, description, albumID)
        else:
            print("check data types")

    def updatePhoto(self, name, description, albumID):
            if (isinstance(name, str) and isinstance(description, str) and isinstance(albumID, int)):
                self.model.updatePhoto(name, description, albumID)
            else:
                print("check data types")

    def insertAlbum(self, name, description, owner):
        if (isinstance(name, str) and isinstance(description, str) and isinstance(owner, str)):
            self.model.insertAlbum(name, description, owner)
        else:
            print("check data types")

    def updateAlbum(self, id, name, description, owner):
        if (isinstance(id, int) and isinstance(name, str) and isinstance(description, str) and isinstance(owner, str)):
            self.model.updateAlbum(id, name, description, owner)
        else:
            print("check data types")

    def deletePhoto(self, id):
        if isinstance(id, str):
            self.model.deletePhoto(id)
        else:
            print("check data types")

    def deleteAlbum(self, id):
        if isinstance(id, int):
            self.model.deleteAlbum(id)
        else:
            print("check data types")

    def getAllPhotos(self):
        print(self.model.getPhotos())

    def getAllAlbums(self):
        print(self.model.getAlbums())

    def getPhotosByAttribute(self, attr, val):
        start_time = datetime.now()
        print(self.model.getPhotosByAttribute(attr, val))
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))

    def getAlbumsByAttribute(self, attr, val):
        start_time = datetime.now()
        print(self.model.getAlbumsByAttribute(attr, val))
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))

    def generateNewAlbums(self, number):
        albms = self.model.getAlbums()
        print(albms)
        print(albms[-1])
        newID = int(albms[-1][0])+1
        names = self.model.getRandomTexts(number, 10)
        descs = self.model.getRandomTexts(number, 20)
        ownrs = self.model.getRandomTexts(number, 7)
        for i in range(int(number)):
            self.model.insertAlbumWithID(newID, names[i], descs[i], ownrs[i])
            newID += 1

    def generateNewPhotos(self, number):
        albms = self.model.getAlbums()
        names = self.model.getRandomTexts(number, 10)
        descs = self.model.getRandomTexts(number, 20)
        numOfAlbms = len(albms)
        aIds = self.model.getRandomInts(numOfAlbms, number)
        print(aIds)
        for i in range(int(number)):
            el = albms[int(aIds[i][0])]
            albmId = int(el[0])
            self.model.insertPhoto(names[i], descs[i], albmId)