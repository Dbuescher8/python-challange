#The total number of months included in the dataset
Month_total =0
#The net total amount of "Profit/Losses" over the entire period
Net_total_PL =0.00


#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
average_profit_loss =0.00

#The greatest increase in profits (date and amount) over the entire period
Greatest_Increase = {}

#The greatest decrease in losses (date and amount) over the entire period
Greatest decrease = {}

import csv
file_path = "./Resources/budget_data.csv"

#result should look like this 
#Financial Analysis
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)
