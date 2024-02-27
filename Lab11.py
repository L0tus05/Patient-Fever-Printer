
# Initialization
patients = []  # List to store patient information

# Sentinel logic to accept input until a blank line is entered
while True:
    input_data = input("Enter patient number and three temperature readings\nEnter blank line to stop entering data\nEnter patient: ")
    if not input_data:  # Check for a blank line to stop entering data
        break

    # Split the input into patient number and temperatures, convert temperatures to float
    patient_data = input_data.split(',')
    patient_number = patient_data[0].strip()
    temperatures = [float(temp) for temp in patient_data[1:]]

    # Calculate average temperature only if temperatures list is non-empty
    avg_temperature = 0.0  # Default value in case temperatures list is empty
    if temperatures:
        avg_temperature = round(sum(temperatures) / len(temperatures), 2)

    # Determine diagnosis based on average temperature
    diagnosis = ""
    if avg_temperature > 98.7:
        diagnosis = "fever"
    elif avg_temperature < 95.0:
        diagnosis = "chilled"

    # Append patient information to the list
    patients.append([patient_number, avg_temperature, diagnosis])

# Output headers
print("\nPT\tAVG\tDiagnosis")

# Loop to print out patient information
for patient in patients:
    print(f"{patient[0]}\t{patient[1]}", end="\t")
    if patient[2]:
        print(patient[2])
    else:
        print()

# Output number of patients
num_patients = len(patients)
print(f"There were {num_patients} patients processed")

# Count patients with fever and chilled diagnoses
fever_count = sum(1 for patient in patients if patient[2] == "fever")
chilled_count = sum(1 for patient in patients if patient[2] == "chilled")

# Calculate and output percentages
if num_patients > 0:
    fever_percentage = round((fever_count / num_patients) * 100, 1)
    chilled_percentage = round((chilled_count / num_patients) * 100, 1)
    print(f"\n{fever_count} had a fever ({fever_percentage}%)")
    print(f"{chilled_count} had a low temperature ({chilled_percentage}%)")
else:
    print("\nThere were 0 patients processed")



# Testing
"""
# Test Case 1
Enter patient number and three temperature readings
Enter blank line to stop entering data
Enter patient: 01111 93.5, 94.0, 97.0
Enter patient: 00222 98.6 98.6 98.7
Enter patient: 00033 99.0 99.0  99.0
Enter patient: 00004 101.0  96.7  98.9
Enter patient: 55550, 98.5, 98.5, 98.6
Enter patient:

PT      AVG      Diagnosis
01111   94.83   chilled
00222   98.63
00033   99.00   fever
00004   98.87   fever
55550   98.53
There were 5 patients processed

2 had a fever (40.0%)
1 had a low temperature (20.0%)

# Test Case 2
Enter patient number and three temperature readings
Enter blank line to stop entering data
Enter patient:

PT      AVG      Diagnosis
There were 0 patients processed

# Test Case 3
Enter patient number and three temperature readings
Enter blank line to stop entering data
Enter patient: 99999, 98.0, 97.0, 97.0
Enter patient: 31345, 97.0, 97.5, 97.0
Enter patient: 12345, 98.0, 97.9, 98.0
Enter patient:

PT      AVG      Diagnosis
99999   97.33
31345   97.17
12345   97.97
There were 3 patients processed

0 had a fever (0.0%)
0 had a low temperature (0.0%)

# Test Case 4
Enter patient number and three temperature readings
Enter blank line to stop entering data
Enter patient: 38428  99.23    96.36   100.22
Enter patient: 81904  96.80    98.73    97.64
Enter patient: 88082 100.10    99.29    99.06
Enter patient: 90449 100.53   100.86   100.43
Enter patient: 79045  98.58    96.97    96.13
Enter patient: 97876  99.24   100.39    99.92
Enter patient: 34887 100.09    97.28    98.66
Enter patient:

PT      AVG      Diagnosis
38428   98.60
81904   97.72
88082   99.48   fever
90449  100.61   fever
79045   97.23
97876   99.85   fever
34887   98.68
There were 7 patients processed

3 had a fever (42.9%)
0 had a low temperature (0.0%)
"""
