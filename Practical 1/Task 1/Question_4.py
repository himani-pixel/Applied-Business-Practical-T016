# Movies only
movie_director = df[df["type"]=="Movie"]["director"].dropna().value_counts()

# TV Shows only
tv_director = df[df["type"]=="TV Show"]["director"].dropna().value_counts()

# Display Director with Highest Movies
print("Director with Highest Number of Movies")
print(movie_director.head(1))

# Display Director with Highest TV Shows
print("\nDirector with Highest Number of TV Shows")
print(tv_director.head(1))

# Display Top 10 Directors
director_count = df["director"].dropna().value_counts()
print("\nTop 10 Directors")
print(director_count.head(10))

# Plot Bar Chart
plt.figure(figsize=(10,5))
director_count.head(10).plot(kind="bar", color="green")
plt.title("Top 10 Directors")
plt.xlabel("Director")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)

plt.show()
