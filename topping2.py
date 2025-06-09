available_toppings =['mushrooms','olives','green peppers','pepperoni','pineapple', 'extra cheese']

requested_toppings =['mushrooms','green peppers','french fries', 'extra cheese']

for reto in requested_toppings:
      if reto in available_toppings:
        print(f"Adding {reto}.")
        
      else:
        print (f"Sorry,we do not have {reto}.")
print ("\nFinished making your Pizza")
