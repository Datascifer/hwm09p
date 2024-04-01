import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        bl = BookLover('Mike', 'test@gmail.com', 'Fiction')
        bl.add_book('Jane Eyre', 4)
        self.assertIn('Jane Eyre', bl.book_list['book_name'].values)

    def test_2_add_book(self):
        bl = BookLover('Susan', 'test@gmail.com', 'Fiction')
        bl.add_book('Jane Eyre', 4)
        bl.add_book('Jane Eyre', 4)  # Attempt to add the same book twice
        self.assertEqual(len(bl.book_list), 1)  # Book should only appear once

    def test_3_has_read(self):
        bl = BookLover('Brenda', 'test@gmail.com', 'Fiction')
        bl.add_book('Jane Eyre', 4)
        self.assertTrue(bl.has_read('Jane Eyre'))

    def test_4_has_read(self):
        bl = BookLover('Jerry', 'test@gmail.com', 'Fiction')
        self.assertFalse(bl.has_read('Moby Dick'))  # Checking a book not in the list

    def test_5_num_books_read(self):
        bl = BookLover('Adam', 'test@gmail.com', 'Fiction')
        bl.add_book('Jane Eyre', 4)
        bl.add_book('Moby Dick', 3)
        self.assertEqual(bl.num_books, 2)  # Verifies the number of books read matches

    def test_6_fav_books(self):
        bl = BookLover('Martin', 'test@gmail.com', 'Fiction')
        bl.add_book('Jane Eyre', 4)
        bl.add_book('Moby Dick', 3) 
        bl.add_book('War and Peace', 5)
        fav_books = bl.fav_books()
        self.assertTrue(all(book['book_rating'] > 3 for index, book in fav_books.iterrows()))  # Checks if all favorite books have a rating above 3
        self.assertIn('War and Peace', fav_books['book_name'].values)
        self.assertNotIn('Moby Dick', fav_books['book_name'].values)

if __name__ == '__main__':
    unittest.main(verbosity=3)
