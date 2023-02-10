import random
print(random.choice('hello'))
print(random.choice((1,2,3,4,5)))
print(random.choice([11,12,13,14,15]))

lottery = [random.randint(1,50) for _ in range(0,50)]
print(lottery)
print(random.sample(lottery,10)) # 10 random values from lottery
print(random.sample(lottery,3))