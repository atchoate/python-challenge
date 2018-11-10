import os
import csv
import numpy

csv_path = os.path.join("Resources", "budget_data.txt")

with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    months = []

    for row in csvreader:
        months.append(row[0])
    
    total_months = len(months)
    print("Total months: " + str(total_months))

print("-------------------------------------------------------------------")

with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    total = []

    for row in csvreader:

        total.append(int(row[1]))
    print("Total: " + str(sum(total)))

print("----------------------------------------------------")

difference = numpy.diff(total)


avg_change = sum(difference) / len(difference)

print("Average change: " + str("{:.2f}".format(avg_change)))
print(max(difference))
print(min(difference))

print("Number of months: " + str(total_months), file=open("budget_results.txt", "a"))
print("-----------------------------------", file=open("budget_results.txt", "a"))
print("Total: " + str(sum(total)), file=open("budget_results.txt", "a"))
print("-----------------------------------", file=open("budget_results.txt", "a"))
print("Average change: " + str("{:.2f}".format(avg_change)), file=open("budget_results.txt", "a"))
print("-----------------------------------", file=open("budget_results.txt", "a"))
print("Greatest increase in profits: " + str(max(difference)), file=open("budget_results.txt", "a"))
print("Greatest decrease in profits: " + str(min(difference)), file=open("budget_results.txt", "a"))