class GotCharacter():
    def __init__(self, first_name = None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

arya = GotCharacter("arya")
unai = Stark("arya")
print(unai.__dict__)