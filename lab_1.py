import unittest
import pickle
data = {
     'ФИО студента': ['Таланов', 'Андрей', 'Александрович'],
     'Номер семестра': ['1', '2', '3', '4'],
     'Название дисциплин': ['Физика', 'Математические методы'],
     'Экзамены': {2, 4}


}

with open('data.pickle', 'wb') as f:
     pickle.dump(data, f)

with open('data.pickle', 'rb') as f:
     data_new = pickle.load(f)


print(data_new)

if __name__ == '__main__':
    unittest.main()


