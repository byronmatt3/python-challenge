# importing dependencies
import os
import csv
# import statistics in order to find the mean later on 
import statistics

# election data in path
Budget_Data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'budget_data.csv')


Month_Count = 0
Total_Volume = 0
Greatest_Increase = 0
Best_Month = ''
Greatest_Decrease = 0
Least_Month = ''

# Create empty lists for the change and month to month change 
Change = []
Month_To_Month_Change = []

with open(Budget_Data_csv, newline='') as csvfile:

    # Delimiter to separate text with comma 
    csvreader = csv.reader(csvfile, delimiter=',')

    # read header 
    csv_header = next(csvreader)
    # Then print the calculated rows 
    for row in csvreader: 
        Month_Count += 1
        Total_Volume += int(row[1])
        if int(row[1]) > Greatest_Increase:
            Best_Month = (row[0])
            Greatest_Increase = int(row[1])
        elif int(row[1]) < Greatest_Decrease:
            Least_Month = (row[0])
            Greatest_Decrease = int(row[1])
        Change.append(int(row[1]))


# Calculate monthly changes 
for i in range(len(Change)-1):
    Monthly_Change = (Change[i+1] - Change[i])
    Month_To_Month_Change.append(Monthly_Change)   

Average_Change = statistics.mean(Month_To_Month_Change)

print("Financial Analysis")
print("___________________________________")

print("Total Months: " + str(Month_Count))
print("Average Change is: $" + str(round(Average_Change, 2)))
print("Total: $" + str(Total_Volume))
print("Greatest Increase in Profits: " + str(Best_Month) + "  ($" + str(Greatest_Increase) + ")")
print("Greatest Decrease in Profits: " + str(Least_Month) + "  ($" + str(Greatest_Decrease) + ")")

f = open("financial_analysis.txt", "w")
f.write("Financial Analysis")
f.write("___________________________________")

f.write("Total Months: " + str(Month_Count))
f.write("Average Change is: $" + str(round(Average_Change, 2)))
f.write("Total: $" + str(Total_Volume))
f.write("Greatest Increase in Profits: " + str(Best_Month) + "  ($" + str(Greatest_Increase) + ")")
f.write("Greatest Decrease in Profits: " + str(Least_Month) + "  ($" + str(Greatest_Decrease) + ")")