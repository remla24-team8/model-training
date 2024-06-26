"""
This module contains test cases for evaluating the invariance of a phishing URL classification model.

MR1: URL Length Invariance
Original Input: http://phishingexample.com/login
Transformed Input: Append a benign path that doesn't change the nature of the URL, 
    e.g., http://phishingexample.com/login?extra=params
Expectation: The classification should remain the same (phishing).

MR2: HTTPS vs. HTTP
Original Input: http://phishingexample.com/login
Transformed Input: Change HTTP to HTTPS, e.g., https://phishingexample.com/login
Expectation: The classification should remain the same (phishing).

MR3: Subdomain Addition
Original Input: http://phishingexample.com/login
Transformed Input: Add a benign subdomain, e.g., http://safe.phishingexample.com/login
Expectation: The classification should remain the same (phishing).

MR4: Parameter Shuffling
Original Input: http://phishingexample.com/login?user=test&session=123
Transformed Input: Shuffle the parameters, e.g., 
    http://phishingexample.com/login?session=123&user=test
Expectation: The classification should remain the same (phishing).

MR5: Case Variation in Path
Original Input: http://phishingexample.com/login
Transformed Input: Change the case of the path, e.g., http://phishingexample.com/LOGIN
Expectation: The classification should remain the same (phishing).

Using data from:
KAITHOLIKKAL, JISHNU K S; B, Arthi  (2024), “Phishing URL dataset”, 
Mendeley Data, V1, doi: 10.17632/vfszbj9b36.1

"""

import os
import json
import numpy as np
from model_service import ModelService

dir_mutaurls = os.path.join(os.path.dirname(__file__), "testdata/mutamorphic_urls.txt")
dir_http100 = os.path.join(os.path.dirname(__file__), "testdata/http_top100.txt")
dir_https100 = os.path.join(os.path.dirname(__file__), "testdata/https_top100.txt")

model = ModelService()

if not os.path.exists(os.path.dirname(__file__) + dir_mutaurls):
    print("Generating Mutamorphic URLs")
    os.system(f"python {os.path.dirname(__file__)}/gen_mutamorphic_data.py")

with open(
    dir_mutaurls,
    "r",
    encoding="UTF-8",
) as data_file:
    all_urls = json.load(data_file)
    original = all_urls["Original"]
    original_pred = np.array(model.predict(original))



def test_url_invariance():
    """
    Tests the model with the same URLs except one has a parameter added,
    to evaluate the invariance to URL length.
    """
    with open(
        dir_mutaurls, 
        "r", 
        encoding='UTF-8',
    ) as file:
        urls = json.load(file)
        mr1 = urls["MR1"]
    mr1_pred = np.array(model.predict(mr1))
    diff_pred = np.abs(original_pred - mr1_pred)
    print("Median difference: ", np.median(diff_pred))
    print(
        "Number of predictions with difference greater than 0.1: ",
        np.sum(diff_pred > 0.1),
    )
    assert np.median(diff_pred) < 0.05


def test_http_v_https():
    """
    Tests the model with the same URLs except one is HTTP and the other is HTTPS,
    to evaluate the invariance to HTTP vs. HTTPS.
    """
    with open(
        dir_http100,
        "r",
        encoding="UTF-8",
    ) as file:
        http_lines = file.readlines()
    with open(
        dir_https100,
        "r",
        encoding="UTF-8",
    ) as file:
        https_lines = file.readlines()
    http_pred = model.predict(http_lines)
    https_pred = model.predict(https_lines)
    print("HTTP median: ", np.median(http_pred))
    print("HTTPS median: ", np.median(https_pred))
    print(
        "Number of HTTP predictions greater than HTTPS: ",
        np.sum(http_pred > https_pred),
    )
    assert np.sum(http_pred > https_pred) > 0.9 * len(http_pred)


def test_subdomain_addition():
    """
    Tests the model with the same URLs except one has a subdomain added,
    to evaluate the invariance to subdomain addition.
    """
    with open(
        dir_mutaurls,
        "r",
        encoding="UTF-8",        
    ) as file:
        urls = json.load(file)
        mr3 = urls["MR3"]
    mr3_pred = np.array(model.predict(mr3))
    diff_pred = np.abs(original_pred - mr3_pred)
    print("Median difference: ", np.median(diff_pred))
    print(
        "Number of predictions with difference greater than 0.1: ",
        np.sum(diff_pred > 0.1),
    )
    assert np.median(diff_pred) < 0.05


def test_parameter_shuffling():
    """
    Tests the model with the same URLs except one has the parameters shuffled,
    to evaluate the invariance to parameter shuffling.
    """
    with open(
        dir_mutaurls,
        "r",
        encoding="UTF-8",
    ) as file:
        urls = json.load(file)
        mr4 = urls["MR4"]
    mr4_pred = np.array(model.predict(mr4))
    diff_pred = np.abs(original_pred - mr4_pred)
    print("Median difference: ", np.median(diff_pred))
    print(
        "Number of predictions with difference greater than 0.1: ",
        np.sum(diff_pred > 0.1),
    )
    assert np.median(diff_pred) < 0.05


def test_case_variation():
    """
    Tests the model with the same URLs except one has the case of the path changed,
    to evaluate the invariance to case variation in the path.
    """
    with open(
        dir_mutaurls,
        "r",
        encoding="UTF-8",
    ) as file:
        urls = json.load(file)
        mr5 = urls["MR5"]
    mr5_pred = np.array(model.predict(mr5))
    diff_pred = np.abs(original_pred - mr5_pred)
    print("Median difference: ", np.median(diff_pred))
    print(
        "Number of predictions with difference greater than 0.1: ",
        np.sum(diff_pred > 0.1),
    )
    assert np.median(diff_pred) < 0.05
