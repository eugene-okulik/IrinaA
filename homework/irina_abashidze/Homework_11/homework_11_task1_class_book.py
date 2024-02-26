class Book:
    def __init__(self, title, author, pages, material, isbn, reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.material = material
        self.isbn = isbn
        self.reserved = reserved

    def details(self):
        if self.reserved:
            print(
                f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, "
                f"материал: {self.material}, зарезервирована")
        else:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, "
                  f"материал: {self.material}")


class Textbook(Book):
    def __init__(self, title, author, pages, material, isbn, subject, grade, has_tasks, reserved=False):
        super().__init__(title, author, pages, material, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.has_tasks = has_tasks

    def details(self):
        if self.reserved:
            print(
                f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, предмет: {self.subject}, "
                f"класс: {self.grade}, зарезервирована")
        else:
            print(
                f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, предмет: {self.subject}, "
                f"класс: {self.grade}")


# Создаем экземпляры книг
book1 = Book("Идиот", "Достоевский", 500, "бумага", "123456789", True)
book2 = Book("Над пропастью во ржи", "Сэлинджер", 400, "бумага", "987654321", False)
book3 = Book("Унесенные ветром", "Митчелл", 600, "бумага", "111222333", False)
book4 = Book("Три мушкетера", "Дюма", 700, "бумага", "444555666", False)
book5 = Book("Приключения Оливера Твиста", "Диккенс", 450, "бумага", "777888999", False)

# Помечаем одну книгу как зарезервированную
book1.reserved = True

# Создаем экземпляры учебников
textbook1 = Textbook("Алгебра", "Иванов", 200, "бумага", "111", "Математика", 9, True)
textbook2 = Textbook("Геометрия", "Мерзляк", 250, "бумага", "222", "Математика", 10, True)
textbook3 = Textbook("Физика", "Генденштейн", 300, "бумага", "333", "Физика", 11, True)
textbook4 = Textbook("История Украины", "Панчук", 150, "бумага", "444", "История", 8, False)
textbook5 = Textbook("География", "Бойко", 180, "бумага", "555", "География", 9, False)

# Помечаем один учебник как зарезервированный
textbook2.reserved = True

# Создаем список книг и учебников
books = [book1, book2, book3, book4, book5]
textbooks = [textbook1, textbook2, textbook3, textbook4, textbook5]

# Выводим информацию о каждой книге и учебнике
for book in books:
    book.details()

for textbook in textbooks:
    textbook.details()
