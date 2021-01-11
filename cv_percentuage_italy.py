import os
import csv

# if you want to test this with your data change * 
#   * file_with_covid -> Replace with the path of your foulder
#   * row -> change the informations inside ['xxx'] -> Example row['daily_cases_in_your_region']

file_with_covidCSV = "/Users/andreistroe/Documents/Research & Data/COVID/COVID-19/dati-regioni/"

# f --> Calculate the Percentage of CASES / TESTS! 
def calculatePercentage(total_daily_cases, total_daily_tests):
    if(int(total_daily_cases) == 0 or int(total_daily_tests) == 0):
         return 0

    return ((int(total_daily_cases) / int(total_daily_tests)) * 100)
     
# f --> Print Results 
def printResult(data, percentage):
    print(str(data) + ": " + str(percentage) + "%")

if __name__ == "__main__":
    total_daily_cases = 0
    total_daily_tests = 0

    # Open Each file in the folder 
    for csv_file in os.listdir(file_with_covidCSV):
        covid_csv = os.path.join(os.path.dirname(file_with_covidCSV), csv_file)
        with open(covid_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # Calculate the total cases and tests did in all Italy regions 
            total_daily_cases = 0
            total_daily_tests = 0

            for row in reader:
                total_daily_cases += int(row['totale_positivi'])
                total_daily_tests += int(row['tamponi'])

            printResult(row['data'], calculatePercentage(total_daily_cases, total_daily_tests))


# TODO -> Using Pytorch or TensorFlow or other stuff... I'll develop an AI to predict when it "Could" end based on the actual data. 

# TODO -> Made it global.

