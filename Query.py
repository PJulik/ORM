import sqlalchemy
from sqlalchemy.orm import sessionmaker

from Models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = f'postgresql://postgres:{password}@localhost:5432/ORM'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

Publisher1 = Publisher(name="Steven King")
Book1 = Book(title="Kerry", publisher=Publisher1)
Shop1 = Shop(name="Буквоед")
Stock1 = Stock(count='5', book=Book1, shop=Shop1)
Sale1 = Sale(price='345.50', date_sale='13.02.2022', count='2', stock=Stock1)

session.add_all([Publisher1, Book1, Shop1, Stock1, Sale1])
session.commit()

id = Publisher.id == input("Введите id издателя ")
q = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Sale).join(Shop).filter(id)
for book, shop, price, date in q:
    print(book, shop, price, date)

session.close()