class Problem(Exception):
  pass
 
class BusinessProblem(Problem):
  pass
 
class CodingProblem(Problem):
  pass
 
def monday_morning():
  try:
    raise Problem
  except CodingProblem:
    print("Will this print?")
 
monday_morning()