from unittest.mock import Mock

mock = Mock(return_value = 25)
print(mock())

stuntman = Mock()
stuntman.jump_off_building.return_value = 123
stuntman.light_on_fire.return_value = 2

print(stuntman.jump_off_building())
print(stuntman.light_on_fire())
