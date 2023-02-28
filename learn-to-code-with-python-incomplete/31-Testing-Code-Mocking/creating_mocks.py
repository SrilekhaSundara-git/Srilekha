from unittest.mock import Mock
# Let's mock a fake Airport object.
# Create a Mock object and assign it to a variable called 'airport'. 
airport = Mock()
# The airport mock should have a 'gates' attribute set to a list of the strings “A1”, “B2”, and “C3”.
airport.gates = ['A1', 'B2', 'C3']
print(airport.gates) 
# The airport mock should have a 'departures' attribute set to a dictionary where 
# the keys are strings representing cities and the 
# values are strings representating their departure times.
airport.departures = { "Atlanta": "12:00PM", "Nashville": "04:30PM"}
print(airport.departures)
# The airport mock should have a 'close' attribute that is callable (i.e. an instance method). 
# When invoked, it should return the string “Closing”.
airport.close.return_value = 'Closting'
print(airport.close())
# The airport should have an 'open' attribute that is callable (i.e. an instance method). .
# When invoked the first time, it should return “Opening…”. 
# When invoked the second time, it should return “Already open”.
airport.open.side_effect = ["Opening...", "Already open", IndexError("List is empty!!!")]
print(airport.open())
print(airport.open())
# EXAMPLE
#
# Given an airport Mock...
#
# print(airport.gates)      # ["A1", "B2", "C3"]
# print(airport.departures) # { "Atlanta": "12:00PM", "Nashville": "04:30PM" }
# print(airport.close())    # Closing
# print(airport.open())     # Opening...
# print(airport.open())     # Already open