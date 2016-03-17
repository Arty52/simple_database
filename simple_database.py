import sys

db = {}
transactions = []

while True:
  # collect input
  command = [x for x in input().strip().split()]
  cmd = command[0]

  if cmd == 'END':
    sys.exit()
  
  if cmd == 'GET':
    name = command[1]
    if name in db:
      print(db[name])
    else:
      print("NULL")
  
  elif cmd == 'UNSET':
    name = command[1]
    db.pop(name, None)
  
  elif cmd == 'SET':
    name, value = command[1], command[2]
    db[name] = value
  
  elif cmd == 'NUMEQUALTO':
    value = command[1]
    print(list(db.values()).count(value))

  elif cmd == 'BEGIN':
    transactions.append(db.copy())

  elif cmd == 'COMMIT':
    transactions = []

  elif cmd == 'ROLLBACK':
    if transactions:
      db = transactions.pop()
    else:
      print("NO TRANSACTION")

  else:
    print("INVALID COMMAND")
