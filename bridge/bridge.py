from abc import ABC, abstractmethod

class Resource(ABC):
    
    @abstractmethod
    def get_summary():
        pass

    @abstractmethod
    def get_image():
        pass

    @abstractmethod
    def get_title():
        pass

    @abstractmethod
    def get_url():
        pass

class AlbumResource(Resource):
    
    def __init__(self, title, artist, songs, url, image):
        self.title = title
        self.artist = artist
        self.songs = songs
        self.url = url
        self.image = image

    def get_summary(self):
        return self.title + ' by: ' + self.artist + '. this album has ' + str(self.songs) + " songs. "

    def get_image(self):
        return self.image

    def get_title(self):
        return self.title

    def get_url(self):
        return self.url

class BookResource(Resource):
    
    def __init__(self, title, author, pages, url, image):
        self.title = title
        self.author = author
        self.pages = pages
        self.url = url
        self.image = image

    def get_summary(self):
        return self.title + ' by: ' + self.author + '. this book has ' + str(self.pages) + " pages. "

    def get_image(self):
        return self.image

    def get_title(self):
        return self.title

    def get_url(self):
        return self.url

class View(ABC):

    def __init__(self, resource: Resource):
        self.resource = resource

    @abstractmethod
    def show():
        pass

class LongformView(View):

    def show(self):
        print("---------------------------")
        print(self.resource.get_title())
        print(self.resource.get_image())
        print(self.resource.get_url())
        print(self.resource.get_summary())
        print("---------------------------")

class ShortformView(View):
    
    def show(self):
        print("---------------------------")
        print(self.resource.get_summary())
        print("---------------------------")


book = BookResource("Penguin Tales", "John Penguinson", 200, "penguintales.com", "I am an image")
album = AlbumResource("Alteralis", "Tol", 12, "alteralis.com", "I am an image")

view1 = LongformView(book)
view2 = ShortformView(book)

view3 = LongformView(album)
view4 = ShortformView(album)

view1.show()
view2.show()
view3.show()
view4.show()