import pytest
from main import BooksCollector

class TestBooksCollector:


    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Преступление и наказание')

        assert len(collector.get_books_genre()) == 2
        assert 'Гордость и предубеждение' in collector.get_books_genre()
        assert 'Преступление и наказание' in collector.get_books_genre()

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Роман')
        assert collector.get_book_genre('Гордость и предубеждение') == 'Роман'

    def test_set_book_genre_invalid(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Новый жанр')
        assert collector.get_book_genre('Гордость и предубеждение') is None

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Роман')
        assert collector.get_book_genre('Гордость и предубеждение') == 'Роман'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Гордость и предубеждение', 'Роман')
        collector.set_book_genre('Преступление и наказание', 'Драма')

        books = collector.get_books_with_specific_genre('Роман')
        assert 'Гордость и предубеждение' in books
        assert 'Преступление и наказание' not in books


    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Гордость и предубеждение', 'Роман')
        collector.set_book_genre('Преступление и наказание', 'Драма')

        books_for_children = collector.get_books_for_children()
        assert 'Гордость и предубеждение' in books_for_children
        assert 'Преступление и наказание' not in books_for_children

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Роман')

        collector.add_book_in_favorites('Гордость и предубеждение')
        assert 'Гордость и предубеждение' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_already_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Роман')

        collector.add_book_in_favorites('Гордость и предубеждение')
        collector.add_book_in_favorites('Гордость и предубеждение')  # Попытка добавить снова
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Роман')
        collector.add_book_in_favorites('Гордость и предубеждение')
        collector.delete_book_from_favorites('Гордость и предубеждение')
        assert 'Гордость и предубеждение' not in collector.get_list_of_favorites_books()


    @pytest.mark.parametrize("book_name", [
        ('Война и мир'),
        ('Отцы и дети'),
        ('Мастер и Маргарита'),
        ('Анна Каренина')
    ])
    def test_add_new_book_parametrized(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()
