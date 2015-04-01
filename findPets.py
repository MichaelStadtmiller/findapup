#!/Users/fhilton/.virtualenvs/petfinder/bin/python
# -- coding: utf-8 --
import petfinder;
# import datetime;
import sqlite3 as lite;
# import sys;
import json;


with open("api_key.json") as json_file:
    api_key = json.load(json_file)
    print(api_key)
    print(api_key["api_key"])

api = petfinder.PetFinderClient(api_key=api_key["api_key"], api_secret=api_key["api_secret"]);


"""breeds = api.breed_list(animal="dog");
print(breeds);
animal = api.pet_getrandom(animal="dog",output="full");
print(animal);
"""
#try:
animal = api.pet_find(animal="dog",location="04350",count=200,size="M");


con = lite.connect('dogs.db')

with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Dogs")
    cur.execute("CREATE TABLE Dogs(id INT, age TEXT, name TEXT, description TEXT, mix TEXT, breeds TEXT,sex TEXT,lastUpdate TEXT,state TEXT, shelterId TEXT)")
    cur.execute("DROP TABLE IF EXISTS Photos")
    cur.execute("CREATE TABLE Photos(dogId INT, url TEXT)")

    i = 1;

    for n in animal:
        print "**********************\n";
        print i;
        print n["name"];
        #print n["photos"][0]["url"]
        #print n["photos"][1]
        #print ','.join(n["photos"][0])

        #print n["description"];
        #print n["age"];
        #print n["mix"];
        #print n["breeds"];
        #print n["id"];
        #print n["sex"];
        #print n["lastUpdate"];
        #print n["contact"]["state"];
        #
        #testing = "test-{0}".format(n["description"].encode('utf-8'))
        #print testing
        #try:
        #sSQL =  "INSERT INTO Dogs VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(n["id"],n["age"],n["mix"],'-'.join(n["breeds"]),n["sex"],n["lastUpdate"],n["contact"]["state"] )

        sSQL =  "INSERT INTO Dogs VALUES(?,?,?,?,?,?,?,?,?,?);"

        print sSQL

        cur.execute(sSQL, (n["id"],n["age"],n["name"],n["description"],n["mix"],'-'.join(n["breeds"]),n["sex"],n["lastUpdate"],n["contact"]["state"],n["shelterId"]))

        for photo in n["photos"]:
            sSQL =  "INSERT INTO Photos VALUES(?,?);"
            cur.execute(sSQL,(n["id"],photo["url"]))
            print sSQL
        con.commit()
            #except:
            #    print "broken"

        #cur.execute("INSERT INTO Dogs VALUES(" + n["id"] + "," + n["name"] + "," + n["description"] + "," + n["age"] + "," + n["mix"] + "," + n["breeds"] + "," + n["sex"] + "," + n["lastUpdate"] + "," + n["contact"]["state"] + ")")

        i=i+1;

#except:
#    print "Done"
#con = lite.connect('dogs.db')
#
#with con:
#    cur.execute("select state,id,breeds,age,lastUpdate from dogs where state='ME'  order by lastUpdate")
#
#    rows = cur.fetchall()
#
#    for row in rows:
#        print "New Row***************"
#        print row
