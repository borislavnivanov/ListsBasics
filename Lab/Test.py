def new():
    raise ValueError
    # return ValueError


for i in range(2):
    try:
        new()
    except ValueError:
        print('Except block')  # Prints on raise only  (Print not executed)
        continue
    print('After Except block')  # Prints on return only (Except block not executed)
