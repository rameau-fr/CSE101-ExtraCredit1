# Name:
# SBUID: 

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# -----------------         Search and sort fruits              -----------------
# TODO: Complete the implementation of listStatistic() and listStd().
# Declare a list of fruit in the main and run the code

def sort_fruits_alphabetically(fruits):
    """ This function sorts fruit by alphabetical order
    
    Args:
        fruits (list): list of fruits
    
    Returns:
        list: sorted list by alphabetical order
    """
    ...

def filter_fruits_by_length(fruits, min_length):
    """ This function filter fruits by string lenth
    
    Args:
        fruits (list): list of fruits
        min_length (int): minimum length for filtering
    
    Returns:
        list: filtered list
    """
    ...

# ---------------------------- Exercise II ---------------------------------------
# -----------------         Second-hand book E-commerce          -----------------
# TODO: Complete the implementation of searchBookTitle(), 
# bubbleSortBooks() and rangeQualityCheckBooks


import csv

def read_books_from_csv(filename):
    """ This function reads the CSV file containing
    the list of Books: Title, Price, Quality, Cover
    
    Args:
        filename (string): relative or absolute path to the csv file
    
    Returns:
        list: nested list
    """
    books = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            title, price, quality, soft_cover = row
            books.append([title, float(price), int(quality), soft_cover == 'Yes'])
    return books

def searchBookTitle(list_book, title):
    """ This function  returns all the books having the name "title"
    Args:
        list_book (list): book database
        title (string): Title of the books you are looking for
    
    Returns:
        list: nested list
    """
    ...

def shakerSortBooks(list_book, what_to_sort, ascending):
    '''
    This function sort book given one of its attribute (either price or quality)
    Args:
        list_book: book database
        what_to_sort : A string representing the field to sort by. i.e. "price" or "quality", otherwise (if any other string is entered) it will sort by price
        order : A bool representing the sort order. True for ascending order or False for descending order.
    '''
    ...
                

def rangeQualityCheckBooks(list_book, quality_range):
    '''
    This function filter book within a quality range (INCLUSIVE)
    Args:
        list_book (list): book database
        quality_range (list): a list with two integer values for the beginning and end range (valid range 0-5)
    '''
    ...

# ---------------------------- MAIN FCT ---------------------------------
def main():

    ########################
    ## Exercise 1 - Fruits ##
    # For the exercise 1 you have to declare a list of fruit
    # And call your functions by yourself



    ########################
    ## Exercise 2 - Books ##
    books = read_books_from_csv('./Books.csv')

    # 1. Search for Harry Potter books
    title = "Harry Potter"
    book_search = searchBookTitle(books, title)
    print("We can find " + str(len(book_search)) + \
          " books called " + title + " in the database ")

    # 2. Sort your book by price using bubble sort
    shakerSortBooks(book_search, "price", True)

    # 3. return only the book with the quality in a given range
    quality_range = [3,5]
    accepted_books = rangeQualityCheckBooks(book_search, quality_range)

    # Display the books
    for book in accepted_books:
        print(book)

if __name__ == "__main__": # do not mind this line, it is something we commonly use in python. You can google
    main() # Here we run the main
