__author__= "Hulk"

import sqlite3
database = sqlite3.connect("sample.db")
print("Database connected !")
c = database.cursor()
print("Cursor created ! ")
#c.execute('''  CREATE TABLE "phone"("id" INTEGER, "Name" TEXT ,"Phone" NUMERIC) ''')
