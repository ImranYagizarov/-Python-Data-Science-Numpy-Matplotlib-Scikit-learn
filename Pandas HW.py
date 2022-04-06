# ДОМАШНЕЕ ЗАДАНИЕ по Pandas
import numpy as np
import pandas as pd

print('ЗАДАНИЕ 1')
# Заданный DataFrame authors:
authors = pd.DataFrame({'author_id': [1, 2, 3],
                        'author_name': ['Тургенев', 'Чехов', 'Островский']},
                       columns=['author_id', 'author_name'])
books = pd.DataFrame({'author_id': [1, 1, 1, 2, 2, 3, 3],
                     'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                     'price': [450, 300, 350, 500, 450, 370, 290]},
                    columns=['author_id', 'book_title', 'price'])
print(authors)
print(books)
print('----------------------------------------------------------')

print('ЗАДАНИЕ 2')
# Соединение DataFrame-ов authors и book по полю author_id:
authors_price = pd.merge(authors, books, on='author_id', how='inner')
print(authors_price)
print('----------------------------------------------------------')

print('ЗАДАНИЕ 3')
# DataFrame authors_price с пятью самыми дорогими:
top5 = authors_price.sort_values(by='price')
print(top5.tail(5))
print('----------------------------------------------------------')

print('ЗАДАНИЕ 4')
# DataFrame authors_stat с самой дорогой и самой дешевой книгой авторов:
df1 = authors_price.groupby('author_name').agg({'price': 'min'}).rename(columns={'price':'min_price'})
df2 = authors_price.groupby('author_name').agg({'price': 'max'}).rename(columns={'price':'max_price'})
df3 = authors_price.groupby('author_name').agg({'price': 'mean'}).rename(columns={'price':'mean_price'})
authors_stat = pd.concat([df1, df2, df3], axis = 1)
print(authors_stat)
print('----------------------------------------------------------')
