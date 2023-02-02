import pandas as pd

# Example list
lst = [1,2,3,4]

# Convert the list to a DataFrame
df = pd.DataFrame(lst)

# Write the DataFrame to a .csv file
df.to_csv("list.csv", index=False)