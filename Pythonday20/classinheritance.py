class Animal:
    def __init__(self):
        self.eye_count = 2

    def breathe(self):
        print("inhale,exhale")
        

class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("doing this under water")


    def swim(self):
        print("swim")

s = Fish()
s.breathe()