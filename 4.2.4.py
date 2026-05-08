import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)
grouped = df.groupby('Date')['Product'].apply(list)

# write the code


pairs = []
for products in grouped:
    if len(products) >= 2:
        pairs.extend(combinations(sorted(products), 2))

# Count frequency of each pair
pair_counts = Counter(pairs)

# Find the most frequent product pair(s)
max_freq = max(pair_counts.values())
most_frequent_pairs = [pair for pair, count in pair_counts.items() if count == max_freq]

# Output the most frequent product pair(s)
for pair in most_frequent_pairs:
    print(f"{pair[0]} and {pair[1]}: {max_freq} times")
