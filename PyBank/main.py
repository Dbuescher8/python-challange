#The total number of months included in the dataset
Month_total = 0
#The net total amount of "Profit/Losses" over the entire period
Net_total_PL = 0.00
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
average_profit_loss = 0.00
#The greatest increase in profits (date and amount) over the entire period
Greatest_Increase = {"date": "", "amount": 0}

#The greatest decrease in losses (date and amount) over the entire period
Greatest_Decrease = {"date": "", "amount": 0}

import csv
file_path = "./Resources/budget_data.csv"

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    for row in csvreader:
        Month_total = Month_total +1
        print(Month_total)
        Net_total_PL = Net_total_PL + float(row[1])
        print(str(Net_total_PL))
        date =row[0]
        profit = float(row[1])
        if (profit> Greatest_Increase["amount"]) 
            Greatest_Increase[date] = date
            Greatest_Increase[amount] = profit
        if (profit < greatest_decrease["amount"]):
            greatest_decrease["date"] = date
            greatest_decrease["amount"] = profit


print("Financial Analysis")
print(---------------------------)
print(f"Total Months: {Month_total}"")
print(
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")








out_file = "./Analysis/output.txt"
with open(out_file, 'w') as outputFile:
    outputFile.write("Financial Analysis")
    outputFile.write("----------------------------")
    outputFile.write(f"Total Months: {Month_total}")
    outputFile.write(f"Total: ${int(Net_total_PL)}")
    outputFile.write(f"Average Change: ${str(round(avg_final,2))}")
    outputFile.write(f"Greatest Increase in Profits: {incrDate} (${int(grIncr)})")
    outputFile.write(f"Greatest Decrease in Losses: {decrDate} (${int(grDecr)})")
    outputFile.write("----------------------------")


#result should look like this 
#Financial Analysis
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)
