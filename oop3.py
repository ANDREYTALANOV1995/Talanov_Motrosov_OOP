from threading import Thread
import time


class student:

    def __init__(self, name, group, faculty, record=[]):
        self.record = record
        self.name = name
        self.group = group
        self.faculty = faculty

    def info(self):
        yield self.name, self.group, self.faculty, self.record

    def add_record(self, discipline, date="12-12-2018", rating=0):
        self.record.append([discipline, date, rating])


class worker(Thread):
    def run(self):
        time.sleep(1)
        print(atm.__next__())


class waiter(Thread):
    def run(self):
        print(atm1.__next__())
        time.sleep(1)


mas = []

mas.append(student('Иван', 'ACY-4', 'ЭТФ'))
mas.append(student('Саша', 'ACY-4', 'ЭТФ'))
mas.append(student('Антон', 'ACY-4', 'ЭТФ'))
mas.append(student('Женя', 'ACY-4', 'ЭТФ'))

atm = mas[0].info()
atm1 = mas[1].info()

worker().start()
waiter().start()
