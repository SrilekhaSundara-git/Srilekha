from unittest.mock import Mock

pizza = Mock()
print(pizza)
print(type(pizza))

# pizza.size = "Large"
# pizza.price = 19.99
# pizza.toppings = ["Mushrooms", "Pineapple", "Apple"]

pizza.configure_mock(
    size = "Large",
    price = 19.99,
    toppings = ["Mushrooms", "Pineaaple", "tofu"]
)

print(pizza.cover_with_cheese())
print(pizza.cover_with_cheese())
print(pizza.size)
print(pizza.price)
print(pizza.toppings)
#print(value)
