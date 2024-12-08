import json
f = open ('name.json')
data = json.load(f)
#result_count = data['places']['place_name']    
#print (result_count)
#d ='V_LIEFER_ID,V_LAUF_ID,SATZNUMMER,EXTRAKTIONSDATUM,'
#d=d.rstrip(",")
#i=0
for i in data['places']:
   print("################# START PRINT" ,i['place name'] ,"######################")
   print (data['country'])
   print ("Country Abbreviation is :",data['country abbreviation'])
   print ("State is :", data['state'])
   print("Place Name is :", i['place name'])
   print ("Place Name is also :",i.get("place name"))
   print("################# END PRINT ######################")
f.close 