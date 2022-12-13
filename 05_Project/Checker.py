from pathlib import Path
import csv
from nltk import sent_tokenize
from sqlalchemy import create_engine as ce
import pandas as pd
from sqlalchemy import inspect

lower_year = input('minimum year?')
higher_year = input('maximum year?')

YEARS = (int(lower_year), int(higher_year))


DATA= Path("books.db")


engine = ce("sqlite:///"+str(DATA))
inspector = inspect(engine)

books_df = pd.read_sql("books", con = engine)
author_df = pd.read_sql("authors", con = engine)
text_df = pd.read_sql("text_files", con = engine)
chapter_df = pd.read_sql("book_file", con = engine)
books_df.sort_values('author_id', inplace=True)
books_df.insert(0, 'year', None, True)
for i in range(len(books_df['author_id'])):
    books_df['year'][i] = min(author_df['born'][books_df['author_id'][i]], author_df['death'][books_df['author_id'][i]])
books_df.sort_values('year', inplace=True)
books_df = books_df[books_df['year']!=10000]
header = ['name', 'line']
look_at = books_df[books_df['year'] > YEARS[0]][books_df['year'] < YEARS[1]]['book_id']
print(len(look_at))
a = input('ok number of books? y/n')
if a == 'n':
  print('stopping')
else:
  with open('book.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for book_id in look_at:
      tokenized = []
      for chapter in chapter_df[chapter_df['book_id'] == book_id]['file_id']:
          book = ' '.join(text_df['text'][chapter].split()).lower()
          tokenized+=sent_tokenize(book)
      for i in range(int((len(tokenized)))):
        writer.writerow(['Books', tokenized[i]])

    """## Get Data from Kaggle"""

    data = pd.read_csv('book.csv')
while True:
    search = input('check for: ')
    for b in data['line']:
        if search in b:
            print(b)