class rectangle:
    def shape(self):
        print("Drawing a rectangle")

class rhombus(rectangle):
    def shape(self):
        print("Drawing a rhombus")

class parallelogram(rectangle):
    def shape(self):
        print("Drawing a parallelogram")

r = rectangle()
r.shape()
rh = rhombus()
rh.shape()
p = parallelogram()
p.shape()
