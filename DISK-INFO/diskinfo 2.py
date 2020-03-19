import os
for root, dirs, files in os.walk("D:"):
    for d in dirs:
        os.chmod(os.path.join(root, d), 0444)
    for f in files:
        os.chmod(os.path.join(root, f), 0444)

