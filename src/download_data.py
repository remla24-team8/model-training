import opendatasets as od

# Assign the Kaggle data set URL into variable
dataset = 'https://drive.google.com/file/d/1MnbhuczVkSjsfYn0xYEu9XR8a9znfvMD/view?usp=sharing'
# Using opendatasets let's download the data sets
od.download(dataset)
