from datetime import datetime 


class Movie:
    def __init__(self, id, title, director, actors, year):
        self.id = id
        self.title = title
        self.director = director
        self.actors = actors
        self.year = year

    def __str__(self):
        return f'{self.id} - {self.title} - {self.director} - {self.actors} - {self.year}'
    

class MovieRepository:
    def __init__(self):
        self.movies = []
        self.id_counter = 1

    def add_movie(self):
        title = input('Unesite naslov filma: ')
        director = input('Unesite redatelja: ')
        actors = input('Unesite glumce: ')
        year = int(input('Unesite godinu: '))

        movie = Movie(self.id_counter, title, director, actors, year)
        self.movies.append(movie)
        self.id_counter += 1
        print(f'Film "{title}" je dodan u biblioteku.\n')
        next_movie = input('Zelite li unjeti novi film? (da/ne): ').lower()
        if next_movie == 'da':
            self.add_movie()

    def movie_list(self):
        return self.movies
    
    def find_movie_by_name(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        return None
        
    def display_library(self):
        for movie in self.movies:
            print(f'ID: {movie.id} -  Naslov: {movie.title}')
            print(f'\t Godina izdavanja: {movie.year}')
            


class RentMovie:
    def __init__(self, client, movie, price, rent_date=None):
        self.client = client
        self.movie = movie
        self.price: int = price
        self.rent_date = rent_date or datetime.now().strftime('%d.%m.%Y')
        self.rented_titles = [movie.title]
        for movie in self.rented_titles:
            print(f'{movie}')

        self.client.add_movie(self.movie)
        

   

    
    def display_rent(self):
        print(f'Korisnik: {self.client.name} {self.client.surname}')
        print(f'Film: {self.movie.title}')
        print(f'Datum iznajmljivanja: {self.rent_date}')
        print(f'Cijena: {self.price}€')
        print(f'Iznajmljeni sadrzaj: {', '.join(self.rented_titles)}')




    def __str__(self):
        return f'{self.client}, {self.movie}, {self.rent_date}, {self.price}€'
    


class Customer:
    def __init__(self, id, name, surname, phone, email, adress):
        self.id = id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.adrress = adress
        self.rented_movies = []

    def add_movie(self, movie):
        self.rented_movies.append(movie)

    def __str__(self):
        return f'{self.id}\n{self.name} {self.surname}\n{self.phone}\n{self.email}\n{self.adrress}'




# Kreiranje repozitorija
repo = MovieRepository()

# Dodajemo film ručno (može se kasnije preko input())
film1 = Movie(1, "Inception", "Christopher Nolan", "Leonardo DiCaprio", 2010)
repo.movies.append(film1)

# Kreiramo korisnika
customer1 = Customer(1, "Pero", "Peric", "0912345678", "pero@gmail.com", "Put Barbira 12")

# Iznajmljivanje filma
rent = RentMovie(customer1, film1, 15)

# Prikaz iznajmljenih filmova
print(f'\nIznajmljeni filmovi korisnika: {customer1.name} {customer1.surname}')
for f in customer1.rented_movies:
    print(f)
print()
rent.display_rent()
