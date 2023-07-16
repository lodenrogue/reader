import sys
import re

def extract_first_sentence(line):
    # Match the first sentence using a regular expression pattern
    pattern = r'^(.*?[.!?])'
    match = re.match(pattern, line)
    
    if match:
        # Extract the first sentence
        return match.group(1)

# Read lines from stdin until the user terminates the input
for line in sys.stdin:
    line = line.strip()

    # Extract and print the first sentence
    sentence = extract_first_sentence(line)

    # Print the original line to stdout
    if sentence:
        print(sentence)

