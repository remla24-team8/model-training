import random


# Number of lines to sample
num_samples = 2500

# List to store the sampled lines
http_lines = []
https_lines = []

# Open the input file
with open('top100.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Check if the line contains 'http' or 'https'
        if 'http://' in line:
            # Add the line to the sampled lines list
            http_lines.append(line.strip())
        if 'https://' in line:
            https_lines.append(line.strip())

# Randomly sample num_samples lines from the sampled lines list
random_samples = random.sample(http_lines, num_samples)

randoms_samples = random.sample(https_lines, num_samples)

with open('http_top100.txt', 'w') as file:
    for line in random_samples:
        file.write(line + '\n')

with open('https_top100.txt', 'w') as file:
    for line in randoms_samples:
        file.write(line + '\n')