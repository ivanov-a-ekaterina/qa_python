from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_init(self):
        collector = BooksCollector
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    @pytest.mark.parametrize('name', ['!№;', 'Книга1 Книга1 Книга1 Книга1 Книга1 Книга1'])
    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('name')
        assert 'name' not in collector.books_genre

    def test_set_book_genre(self):
        collector = BooksCollector()
        name = 'Книга1'
        genre = 'Комедии'
        collector.set_book_genre(name, genre)
        assert name and genre in self.collector.books_genre

    def test_get_book_genre(self):
        collector = BooksCollector()
        name = 'Книга1'
        genre = 'Комедии'
        collector.set_book_genre(name, genre)
        assert name and genre in self.collector.books_genre

    def test_get_book_with_specific_genre(self):
        name1 = 'Книга1'
        name2 = 'Книга2'
        genre = 'Комедии'
        self.collector.set_book_genre(name1, genre)
        self.collector.set_book_genre(name2, genre)
        result = self.collector.get_book_with_specific_genre(genre)
        assert result, [name1, name2]

    def test_add_book_in_favourite(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book_in_favourite('Книга1')
        assert 'Книга1' in collector.get_list_of_favourite_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book_in_favourite('Книга1')
        collector.delete_book_from_favourite('Книга1')
        assert 'Книга1' not in collector.get_list_of_favourite_books()

    def test_get_list_of_favourites(self):
        collector = BooksCollector()
        books = ['Книга1', 'Книга2', 'Книга3']
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favourites(book)
        assert collector.get_list_of_favourites() == books
