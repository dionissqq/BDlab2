from controller import Controller
from model import Model


if __name__ == '__main__':
    myModel = Model()
    myController = Controller(myModel)
    myModel.updatePhoto("newname", "smthreallynew", "newdes",5)
    # myModel.updateAlbum(3, "nova", "desc", "someowner")
    menu=0
    while(int(menu)>=0):
        print("1 - albums")
        print("2 - photos")
        print("0 - exit")
        menu = input()
        if(menu == "1"):
            print("Albums\n")
            print("1 - insert")
            print("2 - update")
            print("3 - delete")
            print("4 - generate random")
            print("5 - getALl")
            print("6 - get by attribute")
            print("0 - exit")
            menu = input()
            if menu == "1":
                print("enter name")
                name = input()
                print("enter description")
                des = input()
                print("enter owner")
                own = input()
                myController.insertAlbum(name, des, own)
            if menu == "2":
                print("enter id")
                id = input()
                print("enter new name")
                name = input()
                print("enter new description")
                des = input()
                print("enter new owner")
                own = input()
                myController.updateAlbum(id, name, des, own)
            if menu == "3":
                print("enter id")
                id = input()
                myController.deleteAlbum(int(id))
            if menu == "4":
                print("enter quantity")
                number = input()
                myController.generateNewAlbums(number)
            if menu == "5":
                myController.getAllAlbums()
            if menu == "6":
                print("enter attribute")
                attr = input()
                print("enter value")
                val = input()
                myController.getAlbumsByAttribute(attr, val)
        if (menu == "2"):
            print("Photos\n")
            print("1 - insert")
            print("2 - update")
            print("3 - delete")
            print("4 - generate random")
            print("5 - getALl")
            print("6 - get by attribute")
            print("0 - exit")
            menu = input()
            if menu == "1":
                print("enter name")
                name = input()
                print("enter description")
                des = input()
                print("enter albumID")
                aId = input()
                myController.insertPhoto(name, des, aId)
            if menu == "2" :
                print("enter name")
                name = input()
                print("enter description")
                des = input()
                print("enter albumID")
                aId = input()
                myController.updatePhoto(name, des, aId)
            if menu == "3":
                print("enter name")
                name = input()
                myController.deletePhoto(name)
            if menu == "4":
                print("enter quantity")
                number = input()
                myController.generateNewPhotos(number)
            if menu == "5":
                myController.getAllPhotos()
            if menu == "6":
                print("enter attribute")
                attr = input()
                print("enter value")
                val = input()
                myController.getPhotosByAttribute(attr, val)
        if(menu == "0"):
            menu=-1
    # myModel.getPhotos()
    # myModel.insertPhoto("sometestName", "desc", "2")
    # myModel.insertAlbum(4, "sometestalbum", "adasd", "someGuy")
    # cur.execute("select usesysid as user_id,usename as username,usesuper as is_superuser,passwd as password_md5,valuntil as password_expiration from pg_shadow order by usename;")
    # answ = cur.fetchall()

