from fastapi import FastAPI

cinema = FastAPI()


movie_genre = {
         'horrors': {
             '1': 'Я - легенда! (8.5)',
             '2': 'Чужой (8.3)',
             '3': 'Мумия (8.3)'
              },
         'drama': {
             '1': 'Зеленая миля (9.1)',
             '2': 'FORD против FERRARI (9.0)',
             '3': '1+1 (9.0)'
              },
         'comedy': {
             '1': 'Круэлла (8.9)',
             '2': 'Король Лев (8.9)',
             '3': 'Душа (8.8)'
              },
         'war': {
             '1': 'По соображениям совести (8.5)',
             '2':  'Храброе сердце (8.5)',
             '3':  'Брестская крепость (8.4)'
              }
              }

full_list = {
         'horrors': {
             '1': {
                 'title': 'Я - легенда!',
                 'Released': '2007',
                 'Producer': 'Френсис Лоуренс',
                 'Rating':   '8.5',
                 'Country':  'USA'
                  },
             '2': {
                 'title': 'Чужой',
                 'Released': '1979',
                 'Producer': 'Ридли Скотт',
                 'Rating':   '8.3',
                 'Country':  'USA'
                  },
             '3': {
                 'title': 'Мумия',
                 'Released': '1999',
                 'Producer': 'Стивен Соммерс',
                 'Rating':   '8.3',
                 'Country':  'USA'
                  }
                  },
         'drama': {
             '1': {
                 'title': 'Зеленая миля',
                 'Released': '1999',
                 'Producer': 'Фрэнк Дарабонт',
                 'Rating':   '9.1',
                 'Country':  'USA'
                  },
             '2': {
                 'title': 'FORD против FERRARI',
                 'Released': '2019',
                 'Producer': 'Джеймс Мэнголд',
                 'Rating':   '9.0',
                 'Country':  'USA'
                  },
             '3': {
                 'title': '1+1',
                 'Released': '2011',
                 'Producer': 'Оливье Накаш, Эрик Толедано',
                 'Rating':   '9.0',
                 'Country':  'France'
                  }
                  },
         'comedy': {
             '1': {
                 'title': 'Круэлла',
                 'Released': '2021',
                 'Producer': 'Крэйг Гиллеспи',
                 'Rating':   '8.9',
                 'Country':  'USA'
                  },
             '2': {
                 'title': 'Король Лев',
                 'Released': '1994',
                 'Producer': 'Роджер Аллерс',
                 'Rating':   '8.9',
                 'Country':  'USA'
                  },
             '3': {
                 'title': 'Душа',
                 'Released': '2020',
                 'Producer': 'Пит Доктер',
                 'Rating':   '8.8',
                 'Country':  'USA'
                  }
                  },
         'war': {
             '1': {
                 'title': 'По соображениям совести',
                 'Released': '2016',
                 'Producer': 'Мэл Гибсон',
                 'Rating':   '8.5',
                 'Country':  'USA'
                  },
             '2': {
                 'title': 'Храброе сердце',
                 'Released': '1995',
                 'Producer': 'Мэл Гибсон',
                 'Rating':   '8.5',
                 'Country':  'USA'
                  },
             '3': {
                 'title': 'Брестская крепость',
                 'Released': '2010',
                 'Producer': 'Александр Котт',
                 'Rating':  '8.4',
                 'Country':  'Russia'
                  }
                  }}


@cinema.get('/')
def main_page():
    greeting = 'Здравствуйте! Добро пожаловать на ' \
               'главную страницу нашего сервиса.' \
               ' Здесь мы можете найти самые лучшие ' \
               'фильмы разных жанров! ' \
               'help: переходите по /movies'
    return greeting


@cinema.get('/movies')
def genre_of_movie():
    return 'Выберите жанр фильма, чтобы выполнить запрос:'\
           ' /horrors - Ужасы, ' \
           ' /drama - Драма,' \
           ' /comedy - Комедия, ' \
           ' /war - Военный, '


@cinema.get('/movies/{genre}')
def open_list(genre):
    if genre in movie_genre:
        if genre == 'horrors':
            return "Вы находитесь в разделе 'Ужасы', " \
               "ниже список фильмов по рейтингу %s, " \
                   "чтобы узнать подробности, переходите по соответствующему  номеру" % movie_genre[genre]
        elif genre == 'drama':
            return "Вы находитесь в разделе 'Драма', " \
                   "ниже список фильмов по рейтингу %s, " \
                   "чтобы узнать подробности, переходите по соответствующему  номеру" % movie_genre[genre]
        elif genre == 'comedy':
            return "Вы находитесь в разделе 'Комедия', " \
                   "ниже список фильмов по рейтингу %s, " \
                   "чтобы узнать подробности, переходите по соответствующему  номеру" % movie_genre[genre]
        else:
            return "Вы находитесь в разделе 'Военный', " \
                   "ниже список фильмов по рейтингу %s, " \
                   "чтобы узнать подробности, переходите по соответствующему  номеру" % movie_genre[genre]
    else:
        return "К сожалению, на нашем сайте, пока нет фильмов по жанру %s (" % genre


@cinema.get('/movies/horrors/{num}')
def open_horrors(num):
    if num in movie_genre['horrors']:
        return "Ваш фильм по запросу: %s " % full_list['horrors'][num]
    else:
        return 'В данном списке не нашлось фильма, по номеру %s' % num


@cinema.get('/movies/drama/{num}')
def open_drama(num):
    if num in movie_genre['drama']:
        return "Ваш фильм по запросу: %s " % full_list['drama'][num]
    else:
        return 'В данном списке не нашлось фильма, по номеру %s' % num


@cinema.get('/movies/comedy/{num}')
def open_comedy(num):
    if num in movie_genre['comedy']:
        return "Ваш фильм по запросу: %s " % full_list['comedy'][num]
    else:
        return 'В данном списке не нашлось фильма, по номеру %s' % num


@cinema.get('/movies/war/{num}')
def open_war(num):
    if num in movie_genre['war']:
        return "Ваш фильм по запросу: %s " % full_list['war'][num]
    else:
        return 'В данном списке не нашлось фильма, по номеру %s' % num
