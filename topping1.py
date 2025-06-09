##requested_toppings =['mushrooms','green peppers', 'extra cheese']
requested_toppings =[]

##if len(requested_toppings) >0:
if requested_toppings:
    for reto in requested_toppings:
      if reto == 'green peppers':
        print ("Sorry,we are out of green peppers right now.")
      else:
        print(f"Adding {reto}")
    print ("\nFinished making your Pizza")
else:
   print("are your sure you want a plain Pizza?")