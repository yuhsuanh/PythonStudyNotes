import pandas as pd

dt = pd.read_csv('ontario transportation company.csv')  
print(dt)  

df = pd.DataFrame(dt)
df.to_csv("test_data.csv")
