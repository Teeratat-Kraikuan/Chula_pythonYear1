u = input().split(", ")
v = input().split(", ")

u[0] = u[0][1:]
u[2] = u[2][:-1]
v[0] = v[0][1:]
v[2] = v[2][:-1]

u[0] = float(u[0])
u[1] = float(u[1])
u[2] = float(u[2])

v[0] = float(v[0])
v[1] = float(v[1])
v[2] = float(v[2])

s = [u[0]+v[0], u[1]+v[1], u[2]+v[2]]

print(u, '+', v, '=', s)
