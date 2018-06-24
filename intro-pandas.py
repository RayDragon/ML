import pandas as pd
data = {
        'name':['Kamal','Govind','Hemant', 'Harry','Rohan'],
        'age':[10,20,30,40, 12],
        'salary':[2600, 9999999999, 99999999, 100000, 0]
        }
obj = pd.DataFrame(data)
print(obj.age)
print(obj['name'])
# print(obj.drop(0), obj.values, '\n' , obj.drop('age', 1))
print(obj.loc([':', 'salary']).scan())