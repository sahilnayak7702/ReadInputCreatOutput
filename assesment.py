import pandas as pd

# Read input files
input1 = pd.read_excel('https://drive.google.com/uc?id=1d2yKbFx9478-73rWRnej95JanYU7j8p_')
input2 = pd.read_excel('https://drive.google.com/uc?id=1dnYGYncRSHzO4UuQ9rB3NWGzZcmSZNIi')

# Count number of statements and reasons
input1['Total'] = input1['Statements'] + input1['Reasons']

# Create output files
output1 = input1.groupby(['Team'])[['Statements', 'Reasons', 'Total']].mean().sum(axis=1).sort_values(ascending=False).reset_index(name='Score')
output2 = input1.groupby(['Name'])[['Statements', 'Reasons', 'Total']].sum().sort_values(by=['Total', 'Name'], ascending=[False, True]).reset_index(drop=True)

# Display output files
print(output1)
print(output2)