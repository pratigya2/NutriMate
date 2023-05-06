import pandas  as pd
import numpy as np
import itertools
import pickle
import numpy as np
DATA = 'home\\static\\meals.csv'

df = pd.read_csv(DATA)
Input = []
#u_input -> 2D
#user_input-> 1D
#input-> only features to model
#
#  

def recommend_meal(user_input):
    saved_model = 'home\\static\\model.pk'
    meals = df.iloc[:, :1].values
    
    recommendation = list()
    
    dis_list = []
    indices_list = []
    
    with open(saved_model, 'rb') as f :
        loaded_model = pickle.load(f)
    
    for u_input in user_input:
        input = u_input[0:3]
        input.append(u_input[5])
        input = [input]
        
        dis, indices = loaded_model.kneighbors(input)
        dis_list.append(dis)
        indices_list.append(indices)
        
        

    combined_dis = np.concatenate(dis_list)
    combined_indices = np.concatenate(indices_list)
    combined_dis= combined_dis.flatten()
    combined_indices= combined_indices.flatten()
    sorted_indices = combined_indices[np.argsort(combined_dis)]    

    
    comb_indices = np.unique(np.array(sorted_indices))
    
    for value in comb_indices:
          recommendation.append(meals[value])
            
    r = np.array(recommendation)
    r = r.flatten()

#     #######
    recommendations = df.loc[df['Nepali Food Name'].isin(r)]

#     #Using the filters
    user_input = u_input
    if(user_input[3]==0.5):
        r1 = recommendations
    else:
        r1 = recommendations[recommendations['Vegetarian']==user_input[3]]

    if (user_input[4]==0.5):
        r2=r1
    else:
        r2 = r1[r1['Dairy-Free']==user_input[4]]

    if (user_input[6]==0.5):
        r3=r2
    else:
        r3 = r2[r2['Oil-Free']==user_input[6]]

    return r3



def create_combinations(array):
    if None not in array:
        return [array]

    combinations = []
    none_indices = [i for i, x in enumerate(array) if x == None]
    for combo in itertools.product([0, 0.25, 0.5, 0.75, 1], repeat=len(none_indices)):
        new_array = list(array)
        for i, value in zip(none_indices, combo):
            new_array[i] = value
        combinations.append(new_array)

    return combinations

#Input from the web part 
def implementation(Input):
    for i in range(0, len(Input)):
        if Input[i]!= None:
            Input[i] = float(Input[i])

    user_inputs = create_combinations(Input)

    meal = recommend_meal(user_inputs)
    meal = (meal['Nepali Food Name']).tolist()
    print(meal)
    return meal