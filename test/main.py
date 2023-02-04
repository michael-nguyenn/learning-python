import pandas as pd

d = {
    "Algorithm": ["Sort 1", "Sort 2", "Sort 3"],
    "random5000": [0.094, 0.025, 0.047],
    "random1000": [0.303, 0.071, 0.164],
    "random50000": [7.220, 0.283, 2.861],
    "reversed5000": [0.074, 0.025, 0.068],
    "reversed10000": [0.227, 0.069, 0.151],
    "reversed50000": [5.305, 0.287, 3.048],
    "sorted5000": [0.041, 0.045, 0.071],
    "sorted10000": [0.068, 0.068, 0.163],
    "sorted50000": [0.002, 0.365, 3.018]
}

df = pd.DataFrame(d)
print(df)
