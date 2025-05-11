import ipdb

 

def calculate_average(scores):
     
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)  
    return average  

scores = [90, 80, 85, 70]  
print("Average score:", calculate_average(scores))
