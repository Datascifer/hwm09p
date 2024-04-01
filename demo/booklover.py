import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=pd.DataFrame({'book_name': [], 'book_rating': []})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name, rating):
        if book_name in self.book_list['book_name'].values:
            print(f"The book '{book_name}' already exists in the book list.")
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            print(f"Book '{book_name}' added successfully.")
            
    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
    
    def list_books(self): # Lists all books in the collection

        return self.book_list.to_string(index=False)
    
    @property # count number of books read
    def num_books(self):
        return len(self.book_list)
    
if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    # And so forth
    