class Problem(Exception):
  pass
 
class BusinessProblem(Problem):
  pass
 
class CodingProblem(Problem):
  pass
 
def monday_morning():
  try:
    raise CodingProblem
  except Problem:
    print("Will this print?")
 
print(monday_morning())