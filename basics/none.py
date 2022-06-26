x = None  # None jest wartością oznaczającą "nic"

print(x)
print(type(x))

# if x == None:
if x is None:  # porówanania z None powinniśmy robić za pomocą operatora `is` lub `is not`
    print("x jest None")
