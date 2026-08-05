# Count content by country
country_count = df["country"].dropna().value_counts()

# Display country with highest content
print("Country with Highest Netflix Content")
print(country_count.head(1))

# Display Top 10 Countries
print("\nTop 10 Countries")
print(country_count.head(10))

# Display Bottom 10 Countries
print("\nBottom 10 Countries")
print(country_count.tail(10))

# Plot Horizontal Bar Chart
plt.figure(figsize=(10,6))
country_count.head(10).sort_values().plot(kind="barh", color="orange")
plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")

plt.show()
