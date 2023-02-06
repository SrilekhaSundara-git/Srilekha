class FilmMaker():
    def give_interview(self):
        print("I love making Movies")

class Director(FilmMaker):
    pass

class ScreenWriter(FilmMaker):
    def give_interview(self):
        print("I Love Writing Scripts")

class JackOfAllTrades(Director, ScreenWriter):
    pass
stallone = JackOfAllTrades()
stallone.give_interview()
print(JackOfAllTrades.mro())