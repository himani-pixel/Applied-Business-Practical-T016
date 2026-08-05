# Separate Movies and TV Shows
movies = df[df["type"]=="Movie"]
tvshows = df[df["type"]=="TV Show"]

# Oldest Movie
print("Oldest Movie")
print(movies[movies["release_year"]==movies["release_year"].min()])

# Newest Movie
print("\nNewest Movie")
print(movies[movies["release_year"]==movies["release_year"].max()])

# Oldest TV Show
print("\nOldest TV Show")
print(tvshows[tvshows["release_year"]==tvshows["release_year"].min()])

# Newest TV Show
print("\nNewest TV Show")
print(tvshows[tvshows["release_year"]==tvshows["release_year"].max()])
