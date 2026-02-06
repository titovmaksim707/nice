class Apple():
    def __init__(self, c, w, s):
        self.color = c
        self.weight = w
        self.mold = 0
        self.sostoyanie = s
        print("Создано!")

    def rot(self, days, temp):
        self.mold = days * temp

app = Apple("красный", 150, "хорошо")
print(app.mold)
app.rot(20, 20)
print(app.mold)
print(app.weight)
print(app.color)
print(app.sostoyanie)
        


