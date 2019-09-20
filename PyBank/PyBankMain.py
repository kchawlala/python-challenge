import os
import csv
import itertools
import numpy as np
budget_csv = os.path.join("budget_data.csv")

# total number of months included in the dataset
total_months = 0

total_amount = 0

pls = []

months = []

#Opening and reading the CSV file
with open(budget_csv, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    
    for row in csvreader:
        total_months += 1
        total_amount = total_amount + float(row[1])
        
        pls.append(float(row[1]))
        months.append(row[0])

avg_change = []
max_change_ind = 0
min_change_ind = 0
max_value = 0
min_value = 0
for i in range(len(pls)):
    if i != 0:
        change = pls[i] - pls[i-1]
        avg_change.append(change)
        if (change) > max_value:
            max_value = change
            max_change_ind = i
        elif change < min_value:
            min_value = change
            min_change_ind = i

print('Financial Analysis\n-----------------------------')
print('Total Months:', total_months)
print('Total: $', total_amount)
print('Average Change: $', round(np.mean(avg_change), 2))
print('Greatest Increase in Profits:', months[max_change_ind], '($', max(avg_change), ')')
print('Greatest Decrease in Profits:', months[min_change_ind], '($', min(avg_change), ')')


#Exporing to .txt file

output1 = open("output2.txt","w")
line1 = "Financial Analysis"
line2 = "---------------------"
line3 = ('Total Months:', total_months)
line4 = ('Total: $', total_amount)
line5 = ('Average Change: $', round(np.mean(avg_change), 2))
line6 = ('Greatest Increase in Profits:', months[max_change_ind], '($', max(avg_change), ')')
line7 = ('Greatest Decrease in Profits:', months[min_change_ind], '($', min(avg_change), ')')
output1.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
output1.close()