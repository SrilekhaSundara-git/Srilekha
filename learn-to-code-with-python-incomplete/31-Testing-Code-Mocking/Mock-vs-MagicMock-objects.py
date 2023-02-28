from unittest.mock import Mock, MagicMock

plain_mock = Mock()
magic_mock = MagicMock()

print(len(magic_mock))
magic_mock.__len__.return_value = 100
print(len(magic_mock))
magic_mock.__getitem__.return_value = 30
print(magic_mock[3])
print(magic_mock[20])
print(magic_mock[0])
if magic_mock:
    print('Hello')
