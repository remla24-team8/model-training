"""
Downloads data from Gdrive and saves it in joblib format.
"""

import sys
from joblib import dump
import gdown


def main():
    """
    Downloads data from Gdrive and saves it in joblib format.

    Usage:
        python src/get_data.py data/train.txt data/test.txt data/val.txt

    Arguments:
        train_data (str): Path to the training data file.
        test_data (str): Path to the testing data file.
        val_data (str): Path to the validation data file.

    Returns:
        None
    """

    if len(sys.argv) != 4:
        sys.stderr.write("Arguments error. Usage:\n")
        sys.stderr.write(
            "\tpython src/get_data.py data/train.txt data/test.txt data/val.txt\n"
        )
        sys.exit(1)
    # Assign the Gdrive data set URL into variable
    dataset = (
        "https://drive.google.com/drive/u/1/folders/1WvOAQXayXZW72ZGUWpTZG5oG9MLwaxpD"
    )

    train_data = sys.argv[1]
    test_data = sys.argv[2]
    val_data = sys.argv[3]

    gdown.download_folder(dataset, output="data")

    # Code to fetch and save data
    with open(train_data, "r", encoding='UTF-8') as file:
        train = [line.strip() for line in file.readlines()[1:]]

    raw_x_train = [line.split("\t")[1] for line in train]
    raw_y_train = [line.split("\t")[0] for line in train]
    dump(raw_x_train, "output/raw_x_train.joblib")
    dump(raw_y_train, "output/raw_y_train.joblib")

    with open(test_data, "r", encoding='UTF-8') as file:
        test = [line.strip() for line in file.readlines()]

    raw_x_test = [line.split("\t")[1] for line in test]
    raw_y_test = [line.split("\t")[0] for line in test]
    dump(raw_x_test, "output/raw_x_test.joblib")
    dump(raw_y_test, "output/raw_y_test.joblib")

    with open(val_data, "r", encoding='UTF-8') as file:
        val = [line.strip() for line in file.readlines()]
    raw_x_val = [line.split("\t")[1] for line in val]
    raw_y_val = [line.split("\t")[0] for line in val]
    dump(raw_x_val, "output/raw_x_val.joblib")
    dump(raw_y_val, "output/raw_y_val.joblib")


if __name__ == "__main__":
    main()
