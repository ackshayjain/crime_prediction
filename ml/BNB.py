#Evaluation of the CrimeCode feature from BPD Crime Dataset using Bernoulli Naive Bayes

from sklearn.naive_bayes import BernoulliNB
import numpy
import pandas as pd
# import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder

bpd_crime_dataframe = pd.read_csv('BPD_Crime_sanitized.csv')


#bpd_crime_dataframe = bpd_crime_dataframe.[~bpd_crime_dataframe.CrimeCode.isin(['8DO', '3LK', '6K', '8FV', '8CV', '3N', '8GV', '8EV', '3EO', '8I', '8CO', '8BV', '8GO', '3EK', '3LO', '3GO'])]
#bpd_crime_dataframe = bpd_crime_dataframe.loc[~bpd_crime_dataframe.CrimeCode.isin(['4E','8DO', '3LK', '6K', '8FV', '8CV', '3N', '8GV', '8EV', '3EO', '8I', '8CO', '8BV', '8GO', '3EK', '3LO', '3GO', '3NF', '1F', '3AK', '3JK', '3CO', '3JF', '3AO', '3AJF', '3NO', '3CK', '3NK', '3GF', '1K', '3AJO', '3AJK', '1O', '3LF', '3GO', '3EK', '3EF', '3LO', '3GK', '3EO', '3LK'])]
#bpd_crime_dataframe = bpd_crime_dataframe.loc[~bpd_crime_dataframe.CrimeCode.isin(['4E', '4C', '3AF', '8DO', '3LK', '6K', '8FV', '8CV', '3N', '8GV', '8EV', '3EO', '8I', '8CO', '8BV', '8GO', '3EK', '3LO', '3GO', '3NF', '1F', '3AK', '3JK', '3CO', '3JF', '3AO', '3AJF', '3NO', '3CK', '3NK', '3GF', '1K', '3AJO', '3AJK', '1O', '3LF', '3GO', '3EK', '3EF', '3LO', '3GK', '3EO', '3LK'])]
bpd_crime_dataframe = bpd_crime_dataframe.loc[~bpd_crime_dataframe.CrimeCode.isin(['4E', '4C', '3AF', '4B', '4A', '4D', '3JO', '8DO', '3LK', '6K', '8FV', '8CV', '3N', '8GV', '8EV', '3EO', '8I', '8CO', '8BV', '8GO', '3EK', '3LO', '3GO', '3NF', '1F', '3AK', '3JK', '3CO', '3JF', '3AO', '3AJF', '3NO', '3CK', '3NK', '3GF', '1K', '3AJO', '3AJK', '1O', '3LF', '3GO', '3EK', '3EF', '3LO', '3GK', '3EO', '3LK'])]

bpd_crime_dataframe = bpd_crime_dataframe.loc[~bpd_crime_dataframe.Neighborhood.isin(['Blythewood', 'The Orchards', 'Bellona-Gittings', 'Taylor Heights', 'Villages of Homeland', 'Curtis Bay Industrial Area', 'Spring Garden Industrial Area', 'Keswick', 'Cedarcroft', 'Greenmount Cemetery', 'Hawkins Point', 'Morgan Park'])]

X = pd.concat([pd.get_dummies(bpd_crime_dataframe['Neighborhood'], prefix = 'NB'), pd.get_dummies(bpd_crime_dataframe['District'], prefix = 'DS'), pd.get_dummies(bpd_crime_dataframe['CrimeHour'], prefix = 'CH'), pd.get_dummies(bpd_crime_dataframe['CrimeDay'], prefix = 'CD')], axis = 1)
#X = pd.concat([pd.get_dummies(bpd_crime_dataframe['District'], prefix = 'DS'), pd.get_dummies(bpd_crime_dataframe['CrimeHour'], prefix = 'CH')], axis = 1)
#X = pd.concat([pd.get_dummies(bpd_crime_dataframe['District'], prefix = 'DS'), pd.get_dummies(bpd_crime_dataframe['CrimeHour'], prefix = 'CH'), pd.get_dummies(bpd_crime_dataframe['CrimeDay'], prefix = 'CD')], axis = 1)

Y = bpd_crime_dataframe['CrimeCode']



from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.002)



#X_train = X.iloc[1:int(len(X)/2)]
#X_test = X.iloc[int(len(X)/2) + 1: len(X)]
#Y_train = Y.iloc[1:int(len(Y)/2)]
#Y_test = Y.iloc[int(len(Y)/2) + 1: len(Y)]

model = BernoulliNB()
model.fit(X_train,Y_train)
#Predictions for the entire test set
Y_pred = model.predict(X_test)

    
score = model.score(X_test,Y_test)
print ('Score for Bernoulli Naive Bayes: ' + str(score*100) + '%')




#Achive List Of classes
classes = model.classes_

#Input 

NeighborhoodName = raw_input("Neighborhood? ")
NeighborhoodHeaders = pd.get_dummies(bpd_crime_dataframe['Neighborhood'], prefix = 'NB')
NeighborhoodHeaders = NeighborhoodHeaders.iloc[1:2]
for i in range(0,len(NeighborhoodHeaders.columns)):
    NeighborhoodHeaders[0:i] = 0
NeighborhoodHeaders['NB_' + NeighborhoodName] = 1


DistrictName = raw_input("District? ")
DistrictHeaders = pd.get_dummies(bpd_crime_dataframe['District'], prefix = 'DS')
DistrictHeaders = DistrictHeaders.iloc[1:2]
for i in range(0,len(DistrictHeaders.columns)):
    DistrictHeaders[0:i] = 0
DistrictHeaders['DS_' + DistrictName] = 1   

 
CrimeHourTime = raw_input("Hour of the Crime? ")
CrimeHourHeaders = pd.get_dummies(bpd_crime_dataframe['CrimeHour'], prefix = 'CH')
CrimeHourHeaders = CrimeHourHeaders.iloc[1:2]
for i in range(0,len(CrimeHourHeaders.columns)):
    CrimeHourHeaders[0:i] = 0
CrimeHourHeaders['CH_'+ CrimeHourTime] = 1


CrimeDayName = raw_input("Crime Day? ")
CrimeDayHeaders = pd.get_dummies(bpd_crime_dataframe['CrimeDay'], prefix = 'CD')
CrimeDayHeaders = CrimeDayHeaders.iloc[1:2]
for i in range(0,len(CrimeDayHeaders.columns)):
    CrimeDayHeaders[0:i] = 0
CrimeDayHeaders['CD_' + CrimeDayName] = 1

#OUTPUT
combo = [NeighborhoodHeaders, DistrictHeaders, CrimeHourHeaders, CrimeDayHeaders]
H = pd.concat(combo, axis=1)
Y_prob = model.predict_proba(H)


for i in range (0,len(set(Y_test))):
    print (classes[i] + ' ' + str(Y_prob[0,i] * 100) )
    

