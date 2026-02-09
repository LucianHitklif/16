baseinp = input("Строка разрешенных ID: ")
allow_set = set(baseinp.split())
incominp = input("Строка входящих ID: ")
incom_list = incominp.split()

for id in incom_list:
    if id in allow_set:
        print("OK")
    else:
        print("ADDED")
        allow_set.add(id)
