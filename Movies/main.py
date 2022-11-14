# Create a class Movie with the following attributes: title, release_year, story_year.
# Create appropriate setter and getter methods.
# Download the comma separated data file:  MarvelMovies.csv
# Create a program that reads in the comma separated data file and loads the data from each line into a Movie object.
# Each line of data contains title, release year, and story year in that order.
# Store the Movie objects in a list.
# Hint: Remember to strip off the newline and split the data using commas.
# Display the movies in alphabetical order. Format the data into columns with appropriate headings.
# Hint: Iterate through a sorted list of the movie titles and use a nested loop to display the details for each movie.

class Movie:
    def __init__(self, title, release_year, story_year):
        self.title = title
        self.release_year = release_year
        self.story_year = story_year

    # Getters and setters
    def get_title(self):
        return self.title

    def get_release_year(self):
        return self.release_year

    def get_story_year(self):
        return self.story_year

    def set_title(self, title):
        self.title = title

    def set_release_year(self, release_year):
        self.release_year = release_year

    def set_story_year(self, story_year):
        self.story_year = story_year


def main():
    if __name__ == '__main__':
        try:
            file = open('MarvelMovies.csv', 'r')
            data = file.read().splitlines()
            movie_list = []

            for movie in data:
                title, re_year, story_year = movie.split(",")
                movie_obj = Movie(title, re_year, story_year)
                movie_list.append(movie_obj)

            movie_list.sort(key=lambda x: x.get_title())

            print(f'{"Title":^35} {"Release":^10} {"Storyline":^10}')
            for movie in movie_list:
                print(f'{movie.get_title():<35} {movie.get_release_year():^10} {movie.get_story_year():^10}')
        except FileNotFoundError:
            print("File Not Found")
main()