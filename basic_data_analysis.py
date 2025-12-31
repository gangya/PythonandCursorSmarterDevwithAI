"""
Get a small dataset, for example a CSV with two columns of numbers (you can create it manually).
Write a parse.py script that reads the CSV (use pandas if you want, Cursor will help you import and use it).
Calculate simple statistics: mean, median, standard deviation for each column.
Generate a scatter plot of one column vs. the other (here you will have to use matplotlib; try asking Cursor "Plot a scatter plot of col1 vs. col2").
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

def start_data_analysis():
    csv_file = input("Enter the path to the CSV file: ")
    try:
        # Create a CSV file if it doesn't exist, with sample data

        if not os.path.exists(csv_file):
            import csv
            with open(csv_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['col1', 'col2'])
                writer.writerow([1, 2])
                writer.writerow([2, 4])
                writer.writerow([3, 6])
                writer.writerow([4, 8])
                writer.writerow([5, 10])
        data = pd.read_csv(csv_file)
        print(data.head())
        print(data.describe())
        print(f"The mean of the data is: {data['col1'].mean()}")
        print(f"The median of the data is: {data['col1'].median()}")
        print(f"The standard deviation of the data is: {data['col1'].std()}")
        plt.title(f"Scatter plot of {csv_file}")
        plt.xlabel('Column 1')
        plt.ylabel('Column 2')
        plt.scatter(data['col1'], data['col2'])
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e} in start_data_analysis function")
    print("Thank you for using the data analysis tool. Goodbye!")
    exit()
    
if __name__ == "__main__":
    start_data_analysis()