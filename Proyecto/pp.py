from ursina import *
app = Ursina()
i=False
print(i)
def input(Key):
    if Key == "e":
        i=True
        print(i)

app.run()
