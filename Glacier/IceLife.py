# Ты можешь определить внутреннее поле.
# 1 - это крестьянин, 0 - пустая ячейка.
innerField = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0],
        [0,0,0,1,1,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0],
        [0,0,0,1,1,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0]
        ]

hero.findNearestEnemy().initField(innerField)

while True:
    # Чтобы избежать бесконечного цикла.
    hero.wait(60)
