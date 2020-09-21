import pandas as pd

feature_names =  ['party','handicapped-infants', 'water-project-cost-sharing', 
                    'adoption-of-the-budget-resolution', 'physician-fee-freeze',
                    'el-salvador-aid', 'religious-groups-in-schools',
                    'anti-satellite-test-ban', 'aid-to-nicaraguan-contras',
                    'mx-missle', 'immigration', 'synfuels-corporation-cutback',
                    'education-spending', 'superfund-right-to-sue', 'crime',
                    'duty-free-exports', 'export-administration-act-south-africa']

voting_data = pd.read_csv('house-votes-84.data.txt', na_values=['?'], 
                          names = feature_names)

# print_load_vote ('voting_data:', voting_data)
# print ('voting_data.describe():')
# print (voting_data.describe())

# Drop Missing Data
voting_data.dropna(inplace=True)
voting_data.describe()

# Replace the string into 1/0
voting_data.replace(('y', 'n'), (1, 0), inplace=True)
voting_data.replace(('democrat', 'republican'), (1, 0), inplace=True)

# print('voting_data.head():')
# print(voting_data.head())

# Generate Features name and classes name
all_features = voting_data[feature_names].drop('party', axis=1).values
all_classes = voting_data['party'].values
print('all_features:')
print(all_features)
print('all_classes:')
print(all_classes)