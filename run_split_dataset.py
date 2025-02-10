import pandas as pd
import json

# Load configuration from JSON file
with open('config.json', 'r') as f:
    config = json.load(f)

def split_excel(input_file, output_file_train, output_file_test, test_size):
    """
    Reads an Excel file, splits the data into training and test sets based on the specified proportion,
    and writes these sets to new Excel files.

    Parameters:
    input_file (str): The path to the input Excel file.
    output_file_train (str): The path to the output Excel file where the training data will be saved.
    output_file_test (str): The path to the output Excel file where the test data will be saved.
    test_size (float): The proportion of the dataset to include in the test split (between 0.0 and 1.0).
    """
    # Read the Excel file
    df = pd.read_excel(input_file)
    
    # Calculate the split index
    total_rows = len(df)
    test_size_rows = int(total_rows * test_size)
    
    # Shuffle the DataFrame rows
    df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Split the DataFrame
    df_test = df_shuffled.iloc[:test_size_rows]
    df_train = df_shuffled.iloc[test_size_rows:]
    
    # Save the train and test data to separate Excel files
    df_train.to_excel(output_file_train, index=False)
    df_test.to_excel(output_file_test, index=False)
    
    print(f"Training file saved as {output_file_train}")
    print(f"Test file saved as {output_file_test}")

# Specify the input and output file names and the test size proportion
input_file = config['dataset_excel_path']
output_file_train = config['output_file_train']
output_file_test = config['output_file_test']
test_size = config['test_size']  # Proportion of the dataset to be used as the test set (between 0.0 and 1.0)

# Call the function to split and save the file
split_excel(input_file, output_file_train, output_file_test, test_size)
