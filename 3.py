serverAinp = input("Ввод (Сервер A): ")
setA = set(serverAinp.split())

serverBinp = input("Ввод (Сервер B): ")
setB = set(serverBinp.split())

comm_file = sorted(setA & setB)
print("Общие ", " ".join(comm_file))

lost_file = sorted(setA - setB)
print("Потерянные ", " ".join(lost_file))
