#Loading the dataset

import pandas as pd

# Code to fetch and save data
train = [line.strip() for line in open("dl-dataset/DL Dataset/train.txt", "r").readlines()[1:10000]]

raw_x_train = [line.split("\t")[1] for line in train]
raw_y_train = [line.split("\t")[0] for line in train]

test = [line.strip() for line in open("dl-dataset/DL Dataset/test.txt", "r").readlines()[1:2000]]
raw_x_test = [line.split("\t")[1] for line in test]
raw_y_test = [line.split("\t")[0] for line in test]

val=[line.strip() for line in open("dl-dataset/DL Dataset/val.txt", "r").readlines()[1:1000]]
raw_x_val=[line.split("\t")[1] for line in val]
raw_y_val=[line.split("\t")[0] for line in val]

# Save data to CSV for further processing
data_train = pd.DataFrame({'text': raw_x_train, 'label': raw_y_train})
data_test = pd.DataFrame({'text': raw_x_test, 'label': raw_y_test})
data_val = pd.DataFrame({'text': raw_x_val, 'label': raw_y_val})

data_train.to_csv('csv_files/train_data.csv', index=False)
data_test.to_csv('csv_files/test_data.csv', index=False)
data_val.to_csv('csv_files/val_data.csv', index=False)

print(len(train), len(test), len(val))
print(len(raw_x_test), len(raw_x_val), len(raw_x_val))