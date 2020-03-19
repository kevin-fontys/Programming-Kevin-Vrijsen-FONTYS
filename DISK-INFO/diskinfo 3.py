import os

path = 'D:\\AA'

folders = []

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for folder in d:
        folders.append(os.path.join(r, folder))

for f in folders:
    print(f)
    p = os.access(f, os.X_OK) # Check for execution access
    print(p," Execute rechten")
    pp = os.access(f, os.W_OK) # Check for execution access
    print(pp," Write rechten")
    ppp = os.access(f, os.R_OK) # Check for execution access
    print(ppp," Read rechten")


# bovenstaande permissie controlen doet het half, graag even meekijken s.v.p.




