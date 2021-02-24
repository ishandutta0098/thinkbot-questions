#Function to find product of consecutive adjacent numbers stored in a list.

def multiply_list(list_x):
  
  mul = list_x[0]                   #store the initial value
  
  for i in range(1, len(list_x)):
    mul = mul*list_x[i]             #multiply with next element in list
    
    yield(mul)                      #yield the result

sample = [1, 2, 3, 4, 5]
result = multiply_list(sample)      #function call

for i in range(len(sample)-1):
  print(next(result))               #print elements stored in yield

#Output:
#2 
#6
#24
#120
