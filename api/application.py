from flask import Flask, request 
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Books.query.all()

    output = []
    for books in books:
        book_data = {'title': Books.title, 'description': Books.description}

        output.append(books_data)
    return {"books": "books data"}


books = [
    {
        'id': 1,
        'book_name': 'Goosebumps',
        'author': 'R.L Stine',
        'publisher': 'Scholastic'
    },
]
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(book)

@app.route('/books', methods=['POST'])
def add_book():
    book = {
        'id': books[-1]['id'] + 1,
        'book_name': request.json['book_name'],
        'author': request.json['author'],
        'publisher': request.json['publisher']
    }
    books.append(book)
    return json(book)

 @app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = [book for book in books if book['id'] == id]
    book[0]['book_name'] = request.json.get('book_name', book[0]['book_name'])
    book[0]['author'] = request.json.get('author', book[0]['author'])
    book[0]['publisher'] = request.json.get('publisher', book[0]['publisher'])
    return jsonify(book[0])

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = [book for book in books if book['id'] == id]
    books.remove(book[0])
    return jsonify({'result': 'Book deleted'})

