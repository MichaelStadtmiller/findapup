import petfinder;
import sqlite3 as lite;
import json;

with open("api_key.json") as json_file:
    api_key = json.load(json_file)
    print(api_key)
    print(api_key["api_key"])

api = petfinder.PetFinderClient(api_key=api_key["api_key"], api_secret=api_key["api_secret"]);

all_breeds = set(api.breed_list(animal='dog'))
bad_breeds = set(['Pit Bull Terrier'])
good_breeds = list(all_breeds - bad_breeds)

#       for pet in api.pet_find(location='45233', animal='dog', count=25):
#               if set(pet['breeds']) - set(bad_breeds):
#                       p.append(pet)
good_breed = {'Bernese Mountain Dog', 'Sheepdog'}
for b in good_breed:
	animal = api.pet_find(aniimal="dog",location="45233",count=200,size="L",age="baby", breed=b);

	con = lite.connect('dogs.db')

	with con:
		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS Dogs")
		cur.execute("CREATE TABLE Dogs(id INT, age TEXT, name TEXT, description TEXT, mix TEXT, breeds TEXT,sex TEXT,lastUpdate TEXT,state TEXT, shelterId TEXT)")
		cur.execute("DROP TABLE IF EXISTS Photos")
		cur.execute("CREATE TABLE Photos(dogId INT, url TEXT)")
	
		i = 1;

		for n in animal:
			print ("**********************\n")
			print (i)
			print (n["name"])

			sSQL =  "INSERT INTO Dogs VALUES(?,?,?,?,?,?,?,?,?,?);"
			# print (sSQL)
			cur.execute(sSQL, (n["id"],n["age"],n["name"],n["description"],n["mix"],'-'.join(n["breeds"]),n["sex"],n["lastUpdate"],n["contact"]["state"],n["shelterId"]))

			for photo in n["photos"]:
				sSQL =  "INSERT INTO Photos VALUES(?,?);"
				cur.execute(sSQL,(n["id"],photo["url"]))
				# print (sSQL)
			con.commit()

			i=i+1;
