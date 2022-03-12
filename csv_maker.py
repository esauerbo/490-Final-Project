import pandas as pd

countydemos = pd.read_csv("county_demographics.csv")
statenames = pd.read_csv("stateCodeToName.csv")

countyWithFullStateNames = countydemos.merge(statenames, left_on="State", right_on="Code")
avgMedIncomeByState = countyWithFullStateNames.groupby('State_y')['Income.Median Houseold Income'].mean().round(decimals=2)
avgMedIncomeByState.to_csv('avgMedIncomePerState.csv')