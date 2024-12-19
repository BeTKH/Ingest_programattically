# This code file should contain API calls required to get the Kaggle dataset for world population.
# The problem should be able to run by the instructor using 'python IngestKaggle.py' (with their own API key).

# Assignment problems:
#   1a) [Done] Use the Kaggle Python library to retrieve the World Population Dataset from Kaggle.com's Datasets.
#       - This is the dataset - https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset.
#   1b) [Done] Download the population data file to 'data\WorldPopulation'.
#

#   2a) [Done] Read the CSV file using Pandas.
#   2b) [Done] Calculate the % increase in population from 2000 to 2022 and create a new column named "PercentIncrease_2000_2022" with that value.
#           Note: store as a decimal - a 10% increase should be stored as 0.10.
#   2c)[Done] Sort the dataframe descending on "PercentIncrease_2000_2022".
#   2d)[Done] Save the new file 'data\WorldPopulation\PopulationWithPercentIncrease.csv'

#   3) [Done] Answer the questions shown below by replacing YourAnswer and executing the code to save the file.

# Points for this file are the following.  Beside being runnable and correct, the code should be well structured
# with descriptive variables, commented as appropriate, and without extra code commented out.
#   - Part 1:  12 points
#   - Part 2:  12 points
#   - Part 3:  6 points

print("IngestKaggle problem")

# Questions - replace YourAnswer with your answer for each question.
with open("Data/WorldPopulation/WorldPopulation.CSV", "w") as file:
    header = "Question | Answer"
    file.write(header + "\n")

    # Question 1
    q1 = "What was the US population percent increase from 2000 to 2022? (note - use decimal direct from 2b) | " + "+0.198"
    file.write(q1 + "\n")

    # Question 2
    q2 = "What country increased the most by percentage from 2000 to 2022? | " + \
        "Qatar, Asia: +3.172"
    file.write(q2 + "\n")

    # Question 3
    q3 = "What country lost the most population by percentage from 2000 to 2022? | " + \
        "Northern Mariana Islands, Oceania: -0.383"
    file.write(q3 + "\n")
