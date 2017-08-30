import os

# Set default path
# default_dir = '/home/ubuntu/deep-learning/nbs/data/kaggle_dogscats'
# training_data_dir = '/train'
default_dir = '/users/chris.lankford/Development/Projects'
training_data_dir = '/bot-chat/'

# Check for train folder existence
directory = default_dir + training_data_dir
if os.path.isdir(directory):
    files = [name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))]
    cats = [name for name in files if "cats" in name]
    print cats


# print(os.path.isdir("/home/ubuntu/deep-learning/nbs/data/kaggle_dogscats/train")
# conditional on whether the path exists or not for train


# Move all files in /train/ with cat.*.jpg to /train/cats/

# Move all files in /train/ with dog.*.jpg to /train/dogs/

# Select 1000 random cat files and move to /valid/cats/ (create /valid/cats/ if it doesn't exist)

# Select 1000 random dog files and move to /valid/dogs/ (create /valid/dogs/ if it doesn't exist)

# Select 10 random cat files from /train/cats/ and copy to /sample/train/cats/ (create /sample/train/cats/ if it
# doesn't exist)

# Select 10 random dog files from /train/dogs/ and copy to /sample/train/dogs/ (create /sample/train/dogs/ if it
# doesn't exist)

# Select 4 random cat files from /valid/cats/ and copy to /sample/valid/cats/ (create /sample/valid/cats/ if it
# doesn't exist)

# Select 4 random dog files from /valid/dogs/ and copy to /sample/valid/dogs/ (create /sample/valid/dogs/ if it
# doesn't exist)
