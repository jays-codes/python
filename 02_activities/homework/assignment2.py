import numpy as np

all_paths = [
  "05_src/data/assignment_2_data/inflammation_01.csv",
  "05_src/data/assignment_2_data/inflammation_02.csv",
  "05_src/data/assignment_2_data/inflammation_03.csv",
  "05_src/data/assignment_2_data/inflammation_04.csv",
  "05_src/data/assignment_2_data/inflammation_05.csv",
  "05_src/data/assignment_2_data/inflammation_06.csv",
  "05_src/data/assignment_2_data/inflammation_07.csv",
  "05_src/data/assignment_2_data/inflammation_08.csv",
  "05_src/data/assignment_2_data/inflammation_09.csv",
  "05_src/data/assignment_2_data/inflammation_10.csv",
  "../05_src/data/assignment_2_data/inflammation_11.csv",
  "../05_src/data/assignment_2_data/inflammation_12.csv"
]

with open(all_paths[0], 'r') as f:
    # YOUR CODE HERE: Use the readline() or readlines() method to read the .csv file into 'contents'
    contents = f.readlines()
    # YOUR CODE HERE: Iterate through 'contents' using a for loop and print each row for inspection
    for line in contents:
        print(line)


def patient_summary(file_path, operation):
    # load the data from the file
    data = np.loadtxt(fname=file_path, delimiter=',')
    ax = 1  # this specifies that the operation should be done for each row (patient)

    # implement the specific operation based on the 'operation' argument
    if operation == 'mean':
        summary_values = np.mean(data, axis=ax)
        # YOUR CODE HERE: calculate the mean (average) number of flare-ups for each patient

    elif operation == 'max':
        summary_values = np.max(data, axis=ax)
        # YOUR CODE HERE: calculate the maximum number of flare-ups experienced by each patient

    elif operation == 'min':
        summary_values = np.min(data, axis=ax)
        # YOUR CODE HERE: calculate the minimum number of flare-ups experienced by each patient

    else:
        # if the operation is not one of the expected values, raise an error
        raise ValueError("Invalid operation. Please choose 'mean', 'max', or 'min'.")

    return summary_values

def check_zeros(x):
    '''
    Given an array, x, check whether any values in x equal 0.
    Return True if any values found, else returns False.
    '''
    # np.where() checks every value in x against the condition (x == 0) and returns a tuple of indices where it was True (i.e. x was 0)
    flag = np.where(x == 0)[0]

    # Checks if there are any objects in flag (i.e. not empty)
    # If not empty, it found at least one zero so flag is True, and vice-versa.
    return len(flag) > 0

# Define your function `detect_problems` here

def detect_problems(file_path):
  #YOUR CODE HERE: use patient_summary() to get the means and check_zeros() to check for zeros in the means
  means = patient_summary(file_path, 'mean')
  if check_zeros(means):
    print("Suspicious looking data")
  else:
    print("Data looks OK")
  return

# test it out on the data file we read in and make sure the size is what we expect i.e., 60
# Your output for the first file should be 60
data_min = patient_summary(all_paths[0], 'min')
print(len(data_min))


# Test out your code here
# Your output for the first file should be False
print(detect_problems(all_paths[0]))

