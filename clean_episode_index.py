from datetime import date
import os
import pandas as pd

# Set index file link
index_file = "./index.txt"

df = pd.DataFrame(columns = ["Title", "Date", "Length", "Episode"])

i = 0

# Create empty lists
titles = []
dates = []
lengths = []
episodes = []

# Parse File based on line numbers
with open(index_file, "r") as file:
    for line in file:
        i += 1
        if (i % 4 == 1):
            # df.at[int(i/4)]["Title"] = line
            print("TITLE: ", line)
            titles.append(line)
        elif (i % 4 == 2):
            line = line.split("|")
            
            dates.append(line[0])
            lengths.append(line[1])
            num = line[2].split("E")[1]
            episodes.append(num)
            print("DATE: ", line[0], "\nLENGTH: ", line[1], "\nEPISODE: ", num)

            # df.at[int(i/4)]["Date"] = line[0]
            # df.at[int(i/4)]["Length"] = line[1]
            # df.at[int(i/4)]["Number"] =  num

# Assign to Dataframe
df["Title"] = titles
df["Date"] = dates
df["Length"] = lengths
df["Episode"] = episodes

df["Title"] = df["Title"].str.strip("\n").str.strip("\"")
df["Date"] = pd.to_datetime(df["Date"])
df["Episode"] = df["Episode"].str.strip("\n")

df = df.set_index(['Episode'])
df = df.sort_values("Date")

df.to_csv("index.csv", header=True, index=True)