"""crea 2 ojetos, que reaccionan distindo al mismo método
, demostrando polimorfismo."""

from bird import Bird, Penguin, let_fly


sparrow = Bird()
penguin = Penguin()
let_fly(sparrow)
let_fly(penguin)
