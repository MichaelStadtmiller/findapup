#!/Users/fhilton/.virtualenvs/petfinder/bin/python
# -- coding: utf-8 --
# import petfinder;
# import datetime;
import sqlite3 as lite;
# import sys;
# import webbrowser as w;
import codecs;
import re;

html_str = """
<html lang="en">
<head>
    <title><!-- Insert your title here --></title>
</head>
<body>
<table>

"""


con = lite.connect('dogs.db')

with con:
    cur = con.cursor()
    #cur.execute("select state,id,breeds,age,lastUpdate from dogs where state in ('ME','NH') and UPPER(breeds) not like '%LAB%' order by lastUpdate desc LIMIT 20")
    #cur.execute("select state,id,breeds,age,lastUpdate from dogs where state in ('ME','NH') and UPPER(breeds) not like '%LAB%' and UPPER(breeds) like '%Retriever%' order by lastUpdate desc LIMIT 20")
    #cur.execute("select state,id,breeds,age,lastUpdate,name,description,breeds,age,mix from dogs where state in ('ME','NH') and UPPER(breeds) not like '%LAB%' order by state, lastUpdate desc LIMIT 20")
    # cur.execute("select state,id,breeds,age,lastUpdate,name,description,breeds,age,mix from dogs where state in ('ME') and UPPER(breeds) not like '%LAB%' order by  lastUpdate desc LIMIT 60")

    cur.execute("""select state,id,breeds,age,lastUpdate,name,description,breeds,age,mix
                from dogs
                where state in ('OH')
                --and description like '%calm%'
                --and description like '%recall%'
                --and description like '%leash%'
                --and age = 'Adult'
                --and shelterId = 'ME89' --Lucky Pup
                --and shelterId = 'ME44' --South Paris
                --and shelterId = 'ME97' --Alpha Dogs
                --and (UPPER(breeds) like '%SPANIEL%'
                --    OR UPPER(breeds) like '%BRITTANY%'
                --    OR UPPER(breeds) like '%BORDER%')
                --and UPPER(breeds) like '%DALMATIAN%'
                order by lastUpdate desc LIMIT 100""")

    #Get all pets for a specific Shelter
    # cur.execute("select state,id,breeds,age,lastUpdate,name,description,breeds,age,mix from dogs where shelterId = 'ME89' order by lastUpdate desc LIMIT 100")

    #cur.execute("select state,id,breeds,age,lastUpdate,name,description,breeds,age,mix from dogs where state in ('ME') and UPPER(breeds) not like '%LAB%' and UPPER(description) like '%SMART%' order by  lastUpdate desc LIMIT 60")


    #cur.execute("select state,id,breeds,age,lastUpdate,name,description,breeds,age,mix from dogs where state in ('ME','NH') and UPPER(breeds) not like '%LAB%' and (UPPER(breeds) like '%SPANIEL%' OR UPPER(breeds) like '%BRITTANY%' OR UPPER(breeds) like '%BORDER%') order by  lastUpdate desc LIMIT 60")


    #cur.execute("select state,id,breeds,age,lastUpdate,name,description,breeds,age,mix from dogs where state in ('ME') and UPPER(breeds) not like '%LAB%' order by lastUpdate desc LIMIT 500")


    rows = cur.fetchall()

    for row in rows:
        #print "New Row***************"
        #print row
        html_str = html_str + "<tr><td>"
        html_str = html_str + "<p>" + str(row[1]) + "<p>"
        html_str = html_str + "<a href=\"https://www.petfinder.com/petdetail/" + str(row[1]) +  "/\">" + str(row[1]) + "<a>"
        html_str = html_str + "<p>" + row[5] + "<p>"
        html_str = html_str + "<p>" + row[6] + "<p>"
        html_str = html_str + "<p>" + row[7] + "<p>"
        html_str = html_str + "<p>Mix:" + row[9] + "<p>"
        html_str = html_str + "<p>" + row[4] + "<p>"
        html_str = html_str + "<p>" + row[3] + "<p>"
        html_str = html_str + "<p>" + row[0] + "<p></td>"

        #w.open('https://www.petfinder.com/petdetail/' + str(row[1]))


        cur2 = con.cursor()
        cur2.execute("select dogId,url from Photos where dogId=?",(row[1],))
        urls = cur2.fetchall()

        #print urls

        #html_str = html_str + "<td>"
        lastId = 0
        maxUrl = ""
        maxWidth = 0

        for url in urls:
            print (url)
            #html_str = html_str + "<strong>" + str(url[0]) + "</strong><img src=\"" + url[1] + "\"/>"
            rCurId =  re.search(r'(bust=)(\d*)',url[1])
            curId = rCurId.group(2)

            rCurWidth =   re.search(r'(width=)(\d*)',url[1])
            curWidth = rCurWidth.group(2)
            print ("width:" + str(curWidth))
            print ("lastID" + str(lastId))
            print ("curID:" + str(curId))
            print ("maxWidth:"+str(maxWidth))
            if lastId != curId:
                if maxUrl != "":
                    print ("newID!")
                    print ("Printing Max URL:" + maxUrl)
                    html_str = html_str + "<td><img src=\"" + maxUrl + "\"/></td>"
                maxUrl = str(url[1])
                lastId = curId
                maxWidth = curWidth
            else:
                print (str(curWidth) + ">" + str(maxWidth))
                if int(curWidth) > int(maxWidth):
                    print ("Setting Max Width:" + str(curWidth))
                    maxWidth = curWidth
                    print ("new Max Width:" + str(maxWidth))
                    maxUrl = str(url[1])
                    print ("Maxwidth:" + str(maxWidth))

            #    if re.findall(r'')

        print ("Printing Max URL:" + maxUrl)
        html_str = html_str + "<td><img src=\"" + maxUrl+ "\"/></td>"


        #html_str = html_str + "<strong>" + str(urls[0][0]) + "</strong><img src=\"" + str(urls[0][1]) + "\"/>"


        #html_str = html_str + "</td>"
        html_str = html_str + "</tr>"



html_str = html_str + """
</table>
</body>
</html>
"""

#print html_str

Html_file= codecs.open("pets.html","w", "utf-8")
Html_file.write(html_str)
Html_file.close()
