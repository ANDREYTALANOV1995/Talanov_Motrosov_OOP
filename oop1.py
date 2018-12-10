import pickle
import unittest

class Za(list):
    point = []

    def __init__(self, name, group):
        self.name = name
        self.group = group

    def add(self, discipline, date, rating=0):
        self.discipline = discipline
        self.date = date
        self.rating = rating
        self.point.append(self.rating)
        self.append([self.discipline, self.date, self.rating])

    def info(self):
        print('#########################################')
        print(self.name + " " + self.group)
        print('_________________________________________')
        for z in self:
            print(z)
        print('_________________________________________')
        print(za.average())
        print('_________________________________________')
        print(za.max())
        print('#########################################')


    def average(self):
        return "Средний бал = " + str(sum(self.point) / self.__len__())

    def max(self):
        string = ""

        print()
        for sel in self:
            if sel[2] == max(self.point):
                string += sel[0] + " "
        return "Легкий предметы = " + string

    def setRating(self, discipline, rating):
        for index, sel, in enumerate(self):
            if sel[0] == discipline:
                sel[2] = rating
                self.point[index] = rating




za = Za("Вася", "ACY-4")


za.add('Программирование', '20.11.2018,', 5)
za.add('Баззы данных', '15.11.2018,', 5)
za.add('Англиский', '15.11.2018,', 5)
za.add('Философия', '15.11.2018', 3)

za.setRating("Англиский", 2)


with open('data1.pickle', 'wb') as f:
    pickle.dump(za, f)

with open('data1.pickle', 'rb') as f:
    za_new = pickle.load(f)

za_new.info()


if __name__ == '__main__':
    unittest.main()
