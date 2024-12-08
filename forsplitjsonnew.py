import json
f = open ('name.json')
data = json.load(f)
#result_count = data['places']['place_name']    
#print (result_count)
#d ='V_LIEFER_ID,V_LAUF_ID,SATZNUMMER,EXTRAKTIONSDATUM,'
#d=d.rstrip(",")
#i=0
for i in data['places']:
   print("Country is :",data['country'])
   print("State is :",data['state'])
   print("State Abbreviation is :",data['state abbreviation'])
   print("Place name is:",  i['place name'])
   print("Post Code is :", i['post code'])
f.close   