# tabel kebenaran (logika bolean)
# and or xor

# NOT
print("*********Logika Not*********")
x = False
y = not x
print("nilai dari x =" , x)
print("nilai dari y =" , x)

# and (hanya bernilai tru, ketika kedua nya true)
# jika ada salah satu saja yang false, maka nilai false
print("\*********LOGIKA AND*********")
x = False
y = False
z = x and y
print(x, "and", y, "=", z)

x = False
y = True
z = x and y
print(x, "and", y, "=", z)

x = True
y = False
z = x and y
print(x, "and", y, "=", z)

x = True
y = True
z = x and y
print(x, "and", y, "=", z)

 # OR (akan bernilai true, selama ada satu aja yang true,)
 # bernilai salah, ketika keduanya salah
 print("\n*********logika OR*********")
x = False
y = False
z = x or y
print(x, "or", y, "=" , z)

x = False
y = False
z = x or y
print(x, "or", y, "=" , z)
