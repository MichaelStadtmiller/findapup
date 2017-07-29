# PetFinderTool
Python scripts that use the petfinder API to create a basic html page listing pets and their info (including pictures)

I got tired of trying to click through the petfinder website, so I took a couple hours and used the petfinder api to create a basic web page containing the pets I was looking for.

The basic idea is:<br>
1. findPets.py uses the api to pull pet info into an sqlite3 database<br>
2. selectPets.py uses a query to select pets from the sqlite3 database and create a basic web page (pets.html)<br>

#Dependancies
You need the followig:<br>
1. Python3
2. Petfinder python library: https://pypi.python.org/pypi/petfinder/ <br>
3. sqlite3: https://www.sqlite.org/

#Usage
1. Get an API key from https://www.petfinder.com/developers/api-key
2. Rename api_key_sample.json to api_key.json. Save your credentials here. (.gitignore will not push api_key.json)
3. Modify the findPets.py find call to include your zipcode etc:
    animal = api.pet_find(animal="dog",location="[yourZipCode]",count=200,size="M");
4. Run the findPets.py script - This creates an sqlite database called dogs.db and fills it with pet info
5. Modify selectPets.py select statement to filter out pets 
6. Run selectPets.py - This creates pets.html
6. Open pets.html with your favorite web browser

#Coders
This was not my own code. I used an API for petfinder and another repository.... I will find and document here soon.
https://github.com/gtaylor/petfinder-api 
