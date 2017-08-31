import os
import numpy as np

# Set default path
# default_dir = '/home/ubuntu/deep-learning/nbs/data/kaggle_dogscats'
default_dir = '/users/chris.lankford/Development/Test/'
training_subdir = 'train/'
validation_subdir = 'valid/'
data_dirs = ['cat', 'dog']
training_dir = default_dir + training_subdir
validation_dir = default_dir + validation_subdir
validation_selection_rate = .25

# Categorize files into training folders per category
# Move all files in /train/ with cat.*.jpg to /train/cats/
# Move all files in /train/ with dog.*.jpg to /train/dogs/

# Check for train folder existence
if os.path.isdir(training_dir):
    # Get a list of the files in the training data directory
    files = [name for name in os.listdir(training_dir) if os.path.isfile(os.path.join(training_dir, name))]
    # Look at each type of data that needs to be categorized
    for t in data_dirs:
        # Get a file list for just the category being iterated on
        file_list = [name for name in files if t in name]
        # Check to see if the destination directory exists already
        if not os.path.isdir(training_dir + t):
            # Create the destination directory
            os.makedirs(training_dir + t)
        # Loop through each file for the specific category
        for f in file_list:
            # Move the file to the categorized folder.
            os.rename(training_dir + f, training_dir + t + '/' + f)

# Select random files to move into the validation set
# Select some number of random cat files and move to /valid/cats/ (create /valid/cats/ if it doesn't exist)
# Select some number of random dog files and move to /valid/dogs/ (create /valid/dogs/ if it doesn't exist)

# Check for validation folder existence
if not os.path.isdir(validation_dir):
    os.makedirs(validation_dir)
for t in data_dirs:
    if not os.path.isdir(validation_dir + t):
        os.makedirs(validation_dir + t)
    file_list = [name for name in os.listdir(training_dir + t)]
    num_files_to_move = int(len(file_list) * validation_selection_rate)
    file_index = np.random.randint(len(file_list), size=num_files_to_move)
    os.rename(training_dir + t + '/' + file_list[file_index], validation_dir + t + '/' + file_list[file_index])




# Select 10 random cat files from /train/cats/ and copy to /sample/train/cats/ (create /sample/train/cats/ if it
# doesn't exist)

# Select 10 random dog files from /train/dogs/ and copy to /sample/train/dogs/ (create /sample/train/dogs/ if it
# doesn't exist)

# Select 4 random cat files from /valid/cats/ and copy to /sample/valid/cats/ (create /sample/valid/cats/ if it
# doesn't exist)

# Select 4 random dog files from /valid/dogs/ and copy to /sample/valid/dogs/ (create /sample/valid/dogs/ if it
# doesn't exist)
