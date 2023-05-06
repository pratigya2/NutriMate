import numpy as np
import random
import pandas as pd
# set the number of arrays to generate
num_arrays = 15000

# create an empty list to hold the arrays
arrays = []
cols = ['Gluten-Free',	'Sugar-Free',	'Keto',	'Vegetarian',	'Dairy-Free',	'Paleo',	'Oil-Free']

# loop to generate each array
for i in range(num_arrays):
    # randomly select the range for the elements
    range_min = 0
    range_max = 10
    # generate the random array
    random_array = np.random.randint(range_min, range_max, size=7)
    
    # randomly set some elements to 0 or 1
    for j in range(7):
        if random.random() < 0.1:   # 10% chance of setting element to 0 or 1
            random_array[j] = random.randint(0, 10)
    
    random_array = random_array/10 
    # append the array to the list
    arrays.append(random_array)

# print the first array for testing
print(arrays)

for array in arrays :
    if array[3]>0.4 :
        array[3]=1
    else:
        array[3]=0
        
    if array[4]>0.35 :
        array[4]= 1
    else:
        array[4]=0
    
    if array[6]>0.5 :
        array[6]=1
    else :
        array[6]=0

arrays= np.array(arrays)
df = pd.DataFrame(arrays, columns=cols)
df.to_csv('dataset_user.csv', index=False)
print('dONE')
#Done