from fastapi import Body
from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {"title": "harry potter", "author": "j.k. rowling", "category": "science"},
    {"title": "lord of the rings", "author": "j.r.r. Tolkien", "category": "science"},
    {"title": "the alchemist", "author": "paulo coelho", "category": "history"},
    {"title": "the da vinci code", "author": "dan brown", "category": "math"},
    {
        "title": "The Little Prince of Mathematics",
        "author": "antoine de saint",
        "category": "math",
    },
    {
        "title": "The Little Prince",
        "author": "antoine de saint",
        "category": "life",
    },
]


@app.get("/")
async def read_all_books():
    return BOOKS


@app.get("/books/{title}")
async def read_book_by_title(title: str):
    """
    Return a book by category.

    Args:
        param (str): The category of the book.

    Returns:
        list: A list of books that belong to the category.
    """
    title = title.casefold()
    return [book for book in BOOKS if book["title"] == title]


@app.get("/books/")
async def read_by_category(category: str):
    """
    Return a book by category.

    Args:
        param (str): The category of the book.

    Returns:
        list: A list of books that belong to the category.
    """
    category = category.casefold()
    return [book for book in BOOKS if book["category"] == category]


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    """
    Return a book by author and category.
    """
    book_author = book_author.casefold()
    category = category.casefold()
    print(book_author, category)

    return [
        book
        for book in BOOKS
        if book.get("author") == book_author and book.get("category") == category
    ]


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    """
    Create a new book.    
    """
    BOOKS.append(new_book)

@app.put("/books/update_book/")
async def update_book(updated_book=Body()):
    """
    Update a book.
    """
    for book in BOOKS:
        if book.get("title").casefold() == updated_book.get("title").casefold():
            book.update(updated_book)
            return book
        
@app.delete("/books/delete_book/")
async def delete_book(title: str):
    for book in BOOKS:
        if book.get("title").casefold() == title.casefold():
            BOOKS.remove(book)
            return book