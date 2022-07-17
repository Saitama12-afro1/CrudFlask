class BookAuthor:
    def __init__(self, book, author, id_book, id_author):
        self.book = book
        self.author = author
        self.id_book = id_book
        self.id_author = id_author
    
    def __repr__(self) -> str:
        return f"{self.book} {self.author}"
    

class ListAuthorBook:
    def __init__(self) -> None:
        self.list_obj  = []
    
    def add(self, obj):
        self.list_obj.append(obj)
    
    
    def all_list_add(self, author):
        for el in author:
            for i in el.books:
                obj = BookAuthor(i, el, i.id, el.id)
                self.add(obj)
        l = self.getList()
        return l
    
    
    def all_list_add_book(self, book):
        for el in book:
            for i in el.authors:
                obj = BookAuthor(el, i, i.id, el.id)
                self.add(obj)
        l = self.getList()
        return l
        
    
    def getList(self):
        return self.list_obj

    

    
    