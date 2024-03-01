class Flower:
    stem_length = 45  # Общее свойство класса - длина стебля для всех цветов
    has_scent = True  # Общее свойство класса - наличие аромата для всех цветов

    def __init__(self, color, freshness, stem_length, wilting_time, price):
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        # self.has_scent = self.has_scent
        self.wilting_time = wilting_time
        self.price = price

    def details(self):
        return f"{self.color} цвет, свежесть: {self.freshness}, длина стебля: {self.stem_length} см, " \
               f"время увядания: {self.wilting_time} дней, стоимость: {self.price} грн"


class Lily(Flower):
    def __init__(self, color, freshness, stem_length, wilting_time, price):
        super().__init__(color, freshness, stem_length, wilting_time, price)


class Peony(Flower):
    def __init__(self, color, freshness, stem_length, wilting_time, price):
        super().__init__(color, freshness, stem_length, wilting_time, price)


class Rose(Flower):
    def __init__(self, color, freshness, stem_length, wilting_time, price):
        super().__init__(color, freshness, stem_length, wilting_time, price)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_average_wilting_time(self):
        if not self.flowers:
            return 0

        total_wilting_time = sum(flower.wilting_time for flower in self.flowers)
        average_wilting_time = total_wilting_time / len(self.flowers)
        return average_wilting_time

    def sort_flowers(self, key):
        self.flowers.sort(key=key)

    def search_flowers_by_freshness(self, target_freshness):
        return [flower for flower in self.flowers if flower.freshness == target_freshness]

    def details(self):
        for flower in self.flowers:
            print(flower.details())


# Пример использования
lily1 = Lily("white", "fresh", 35, 8, 50)
peony1 = Peony("pink", "medium", 30, 10, 55)
rose1 = Rose("red", "fresh", 40, 6, 60)

bouquet = Bouquet()
bouquet.add_flower(lily1)
bouquet.add_flower(peony1)
bouquet.add_flower(rose1)

# Вычисляем и выводим среднее время увядания
average_wilting_time = bouquet.calculate_average_wilting_time()
print(f"Среднее время увядания в букете: {average_wilting_time} дней")

# Сортируем и выводим букет по длине стебля
bouquet.sort_flowers(key=lambda flower: flower.stem_length)
print("\nОтсортированный букет по длине стебля:")
bouquet.details()

# Сортируем и выводим букет по стоимости
bouquet.sort_flowers(key=lambda flower: flower.price)
print("\nОтсортированный букет по стоимости:")
bouquet.details()

# Ищем и выводим цветы 'fresh'
fresh_flowers = bouquet.search_flowers_by_freshness("fresh")
print("\nЦветы 'fresh':")
for flower in fresh_flowers:
    print(flower.details())
