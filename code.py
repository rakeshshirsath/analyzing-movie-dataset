# --------------
from csv import reader
def explore_data(dataset, start, end, rows_and_columns=False):
    """Explore the elements of a list.
    Print the elements of a list starting from the index 'start'(included) upto the          index 'end' (excluded).
    Keyword arguments:
    dataset -- list of which we want to see the elements
    start -- index of the first element we want to see, this is included
    end -- index of the stopping element, this is excluded 
    rows_and_columns -- this parameter is optional while calling the function. It takes      binary values, either True or False. If true, print the dimension of the list, else      dont."""
    dataset_rows = dataset[start:end]
    for row in dataset:
        print(row,"\n")
    print("Number of Rows",len(dataset_rows))
    print("number of Columns",len(dataset_rows[0]))

def duplicate_and_unique_movies(dataset, index_):
    """Check the duplicate and unique entries.
    
    We have nested list. This function checks if the rows in the list is unique or           duplicated based     on the element at index 'index_'.
    It prints the Number of duplicate entries, along with some examples of duplicated        entry.
    
    Keyword arguments:
    dataset -- two dimensional list which we want to explore
    index_ -- column index at which the element in each row would be checked for             duplicacy 
    
    """ 
    duplicate_movies = []
    unique_movies =[]

    for row in dataset:
        movie_name = row[index_]
        if movie_name in unique_movies:
            duplicate_movies.append(movie_name)
        else:
            unique_movies.append(movie_name)
    print("number of duplicate movies are - ",len(duplicate_movies))  

def movies_lang(dataset, index_, lang_):
    """Extract the movies of a particular language.
    Of all the movies available in all languages, this function extracts all the movies      in a particular laguage.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.

    Keyword arguments:
    dataset -- list containing the details of the movie
    index_ -- index which is to be compared for langauges
    lang_ -- desired language for which we want to filter out the movies
    
    Returns:
    movies_ -- list with details of the movies in selected language
    
    """
    movies_ = []
    for row in movies:
        lang=row[index_]
        if lang == lang_:
            movies_.append(row)
    print("Examples of english movies are -",explore_data(movies_,0,3,True))
    return movies_

def rate_bucket(dataset, rate_low, rate_high):
    """Extract the movies within the specified ratings.
    
    This function extracts all the movies that has rating between rate_low and high_rate.
    Once you have extracted the movies, call the explore_data() to print first few rows.
    
    Keyword arguments:
    dataset -- list containing the details of the movie
    rate_low -- lower range of rating
    rate_high -- higher range of rating
    
    Returns:
    rated_movies -- list of the details of the movies with required ratings
    """
    rated_movies = []
    for row in dataset:
        vote = float(row[11])
        if rate_low <= vote <= rate_high:
            rated_movies.append(row)

    print("Examples of Movies in required rating bucket:")   
    explore_data(rated_movies, 0, 3, True)

    return rated_movies

# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)

# The first row is header. Extract and store it in 'movies_header'.
movies_header = movies[0]
print("Movies Header is \n", movies_header)

# Subset the movies dataset such that the header is removed from the list and store it back in movies
movies = movies[1:]

# Delete wrong data
del movies[4553]
# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.
# Using explore_data() with appropriate parameters, view the details of the first 5 movies.
explore_data(movies, 0, 5, rows_and_columns=False)

# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.
#print("header",movies_header)
duplicate_index = movies_header.index("title_movies")
duplicate_and_unique_movies(movies, duplicate_index)

# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.
reviews_max = {}
for row in movies:
    movies_name = row[duplicate_index]
    movie_review = row[duplicate_index - 1]
    if movies_name in reviews_max and reviews_max[movies_name] < movie_review:
        reviews_max[movies_name] = movie_review
    elif movies_name not in reviews_max:
        reviews_max[movies_name] = movie_review
print("length of review_max is -",len(reviews_max))

# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 
movies_clean = []
unique_movies_name = []
for row in movies:
    movie_name = row[duplicate_index]
    movie_review = row[duplicate_index - 1]
    if (movie_review == reviews_max[movie_name]) and movie_name not in unique_movies_name:
        movies_clean.append(row)
        unique_movies_name.append(movie_name)
len(movies_clean)

# Calling movies_lang(), extract all the english movies and store it in movies_en.
movies_eng = movies_lang(movies,3,'en')

# Call the rate_bucket function to see the movies with rating higher than 8.
high_rated_movies = rate_bucket(movies_eng,8,10)




