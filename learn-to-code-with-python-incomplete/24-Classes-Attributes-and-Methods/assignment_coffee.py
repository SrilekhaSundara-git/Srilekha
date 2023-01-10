class Coffee:
    def __init__(self, cream, sugar, half_and_half):
        self.cream = cream
        self.sugar = sugar
        self.half_and_half = half_and_half
 
 
morning_joe = Coffee(True, False, True)
 
for val in [
    "cream",
    "pumpkin spice",
    "cinnamon",
    "sugar",
    "half_and_half",
]:
    if hasattr(morning_joe, val):
        setattr(
            morning_joe, val, not getattr(morning_joe, val)
        )
 
print(
    morning_joe.cream,
    morning_joe.sugar,
    morning_joe.half_and_half,
)