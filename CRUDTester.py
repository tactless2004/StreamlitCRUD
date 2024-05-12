from documentHolder import DocumentHolder

db = DocumentHolder()

# Test 1: insert and read together
db.insert("Example Record")
assert(db.read(0)=="Example Record")
assert(db.read(1)=="Document does not exist!") 

db.insert("Example Record 2")
assert(db.read(1)=="Example Record 2")
print("Test 1 passed!")

db.clear() # Clear the database state between tests.

# Test 2: rigorous insert and read together, then test listAll
for i in range(0,101):
    value = "Example Record {0}".format(i)
    db.insert(value)
    assert(db.read(i) == value)
db.listAll()

db.clear() # Clear the database state between tests.
print("Test 2 passed!")

# Test 3: test delete
for i in range(0,101):
    value = "Example Record {0}".format(i)
    db.insert(value)
    assert(db.read(i) == value)
    db.delete(i)
    assert(db.read(i) == "Document does not exist!")

db.clear()

print("Test 3 passed!")

# Test 4: test update
for i in range(0,101):
    value = "Example Record {0}".format(i)
    db.insert(value)
    assert(db.read(i) == value)

    newvalue = "New Example Record {0}".format(i)
    db.update(id = i, newbody=newvalue) 
    assert(db.read(i) == newvalue)

print("Test 4 passed!")