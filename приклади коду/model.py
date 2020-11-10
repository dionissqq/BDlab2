import psycopg2
from datetime import datetime


class Model(object):

    def __init__(self):
        self.conn = psycopg2.connect("dbname=MyDB user=postgres password=postgrepass host=localhost")
        self.cur = self.conn.cursor()

    def getPhotos(self):
        self.cur.execute("SELECT * FROM public.\"Photos\"")
        answ=self.cur.fetchall()
        return answ

    def getAlbums(self):
        self.cur.execute("SELECT * FROM public.\"Albums\"")
        answ=self.cur.fetchall()
        return answ

    def insertPhoto(self, name, description, albumID):
        self.cur.execute("INSERT INTO public.\"Photos\"(name, description, \"albumid\") VALUES (%s, %s, %s);", (name, description, albumID))
        self.conn.commit()

    def insertAlbum(self, name, description, owner):
        date = datetime.today()
        albms = self.getAlbums()
        newID = int(albms[-1][0])+1
        self.cur.execute("INSERT INTO public.\"Albums\"(id, date, name, description, owner) VALUES (%s, %s, %s, %s, %s);", (newID, date, name, description, owner))
        self.conn.commit()

    def insertAlbumWithID(self, id, name, description, owner):
        date = datetime.today()
        self.cur.execute("INSERT INTO public.\"Albums\"(id, date, name, description, owner) VALUES (%s, %s, %s, %s, %s);", (id, date, name, description, owner))
        self.conn.commit()

    def updatePhoto(self, oldname, name, description, albumID):
        self.cur.execute("UPDATE public.\"Photos\" SET name=%s, description=%s, albumid=%s WHERE name=%s;", (name, description, albumID, oldname))
        self.conn.commit()

    def updateAlbum(self, id, name, description, owner ):
        self.cur.execute("UPDATE public.\"Albums\" SET name=%s, description=%s, owner=%s WHERE id=%s;",
                         (name, description, owner, id))
        self.conn.commit()

    def deletePhoto(self, name):
        self.cur.execute("DELETE FROM public.\"Photos\" WHERE name=%s;", (name))
        self.conn.commit()

    def deleteAlbum(self, id):
        self.cur.execute("DELETE FROM public.\"Albums\" WHERE id=%s;", (str(id)))
        self.cur.execute("DELETE FROM public.\"Photos\" WHERE albumid = %s;", (str(id)))
        self.conn.commit()

    def getRandomInts(self, max, number):
        self.cur.execute("SELECT trunc(random()*%s)::int FROM generate_series(1, %s)", (max, number))
        answ = self.cur.fetchall()
        return answ

    def getRandomTexts(self, number , length):
        self.cur.execute("select randomText(%s) from generate_series(1,%s)", (length, number))
        answ = self.cur.fetchall()
        return answ

    def getPhotosByAttribute(self, attr, val):
        if attr == "albumid":
            print("hi")
            self.cur.execute("select * FROM public.\"Photos\" WHERE albumid = "+val)
            return self.cur.fetchall()
        self.cur.execute("select * FROM public.\"Photos\" WHERE %s LIKE %s", (attr, val))
        return self.cur.fetchall()

    def getAlbumsByAttribute(self, attr, val):
        if attr == "id":
            self.cur.execute("select * FROM public.\"Albums\" WHERE id = "+val)
            return self.cur.fetchall()
        self.cur.execute("select * FROM public.\"Albums\" WHERE %s LIKE %s", (attr, val))
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()
