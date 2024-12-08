from f1_n import f1 

#lst = [1,2,3,5,8,10,100]
lst = ['ASS_AG91','ASS_AG92','ASS_AG95','ASS_AG96','ASS_AG97','ASS_AG99','ASS_AG81']
w = 0
for i in lst:
  w += 1
  print('LEERZEILE')
  print (w)
  if i=='ASS_AG95':
    print ('#################### f1 START ####################################')
    print('HURRA! Der eingegebene Wert ist ASS_AG95')
    x= 25
    f1(x)
    print ('#################### f1 ENDE #####################################')
   
  else:
   print('Der eingebene Wert Lautet:', i)
   print('Der {}. Wert: {}'.format(w,i))
  