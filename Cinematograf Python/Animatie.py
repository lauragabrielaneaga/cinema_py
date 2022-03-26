from Film import Film

class Animatie(Film):
    limba_dublare = ""
    def __init__(self,titlu, durata, limba_dublare):
        super().__init__(titlu, durata)
        self.limba_dublare = limba_dublare

    def dublare(self):
        return self.limba_dublare