#Task1
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("NetFlix.csv")

# Count the number of titles in each genre
genre_count = df["genres"].value_counts()

# Display Top 10 Genres
print("Top 10 Genres")
print(genre_count.head(10))

# Display Bottom 10 Genres
print("\nBottom 10 Genres")
print(genre_count.tail(10))

# Display Most Popular Genre
print("\nMost Popular Genre")
print(genre_count.idxmax(), "-", genre_count.max())

# Display Least Popular Genre
print("\nLeast Popular Genre")
print(genre_count.idxmin(), "-", genre_count.min())

# Plot Top 10 Genres
plt.figure(figsize=(10,5))
genre_count.head(10).plot(kind="bar", color="skyblue")

plt.title("Top 10 Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.show()
