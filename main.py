import json

code = input("Code: ")

f = open("./data/directions.json")

fdata = json.load(f)

data = fdata[code]

def CheckDir(userIn, data):
    for k, v in data.items():
        for obj in data[k]:
            if(userIn.lower() == obj.lower()):
                return k
    return False

userIn = input("Inserire oggetto: ")

print(CheckDir(userIn, data) if CheckDir(userIn, data) else "Nessun elemento trovato")