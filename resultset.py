dict = { 'a' :12, 'c' :78, 'b' :3, 'd' :43}
resultset = { x for x in dict}
print (resultset)
resultlist ={ k: v for k,v in dict.items()}
print (resultlist)
print ("Der Wert für a ist: ",dict['a'])
