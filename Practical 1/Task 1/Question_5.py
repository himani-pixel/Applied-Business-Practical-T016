# Count releases
before_2020 = df[df["release_year"] < 2020].shape[0]
during_2020 = df[df["release_year"] == 2020].shape[0]
after_2020 = df[df["release_year"] > 2020].shape[0]

# Create DataFrame
release_data = pd.DataFrame({
   "Period":["Before 2020","During 2020","After 2020"],
   "Count":[before_2020,during_2020,after_2020]
})
print(release_data)

# Plot Bar Chart
plt.figure(figsize=(7,5))
plt.bar(release_data["Period"], release_data["Count"], color=["blue","orange","green"])
plt.title("Netflix Releases Comparison")
plt.xlabel("Period")
plt.ylabel("Number of Titles")

plt.show()
