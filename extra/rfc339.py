from datetime import datetime, timezone

hora_local = datetime.now(timezone.utc).astimezone().isoformat()

# print(hora_local)

a = [['a', 'n', 'd', 'e', 's'], ['c', 'a', 'c', 'a']]
n_a = []
 
for palabra in a:
    palabra = ''.join(palabra)
    n_a.append(palabra)

print(n_a)