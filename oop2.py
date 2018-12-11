import pickle
import unittest
from datetime import datetime


class Record:
    def __init__(self, discipline, date=datetime.now(), rating=0):

        try:
            if rating > 5 or rating < 0:
                raise RatingException()
            else:
                self.rating = rating

        except RatingException:
            print("Неправильная оценка")

        self.discipline = discipline
        self.date = date


    def setDateRating(self, date, rating):
        self.date = date

        try:
            if rating > 5 or rating < 0:
                raise RatingException()
            else:
                self.rating = rating

        except RatingException:
            print("Неправильная оценка")

    def __str__(self):
        return self.discipline + "|" + str(self.date) + "|" + str(self.rating)


class Student:
    def __init__(self, first_name, surname, group, faculty, record_book=[]):
        self.first_name = first_name
        self.surname = surname
        self.group = group
        self.faculty = faculty
        self.record_book = record_book

    def info(self):
        print(self.first_name + "|" + self.surname + "|" + self.group + "|" + self.faculty)
        for rec in self.record_book:
            print(rec)

    def setRecord(self, record):
        self.record_book = record

    def getRecord(self):
        return self.record_book


class Discipline:
    def __init__(self, name, lecturer, hours):
        self.name = name
        self.lecturer = lecturer
        self.hours = hours

    def getName(self):
        return self.name

    def info(self):
        print(self.name, self.lecturer, self.hours)

class RatingException(Exception):

    def __init__(self):
        Exception.__init__(self)


record = []
discipline = []

discipline.append(Discipline("Программирование", "Иванов И.И.", 120))
discipline.append(Discipline("Баззы данных    ", "Иванов И.И.", 120))
discipline.append(Discipline("Англиский       ", "Иванов И.И.", 120))
discipline.append(Discipline("Философия       ", "Иванов И.И.", 120))

for disc in discipline:
    record.append(Record(disc.getName()))

student = Student('Иван', 'Иванов', 'ACY-4', 'ETF')

student.setRecord(record)

student.getRecord()[0].setDateRating("2018-11-12",5)

with open('data2.pickle', 'wb') as f:
    pickle.dump(student, f)
    pickle.dump(discipline, f)

with open('data2.pickle', 'rb') as f:
    student_new = pickle.load(f)
    discipline_new = pickle.load(f)
student_new.info()
