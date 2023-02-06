def experiment():
  try:
    raise ValueError
  except TypeError:
    print("Zebra")
  except IndexError:
    print("Kangaroo")
  except ValueError:
    print("Aardvark")
  else:
    print("Koala")
 
print(experiment())