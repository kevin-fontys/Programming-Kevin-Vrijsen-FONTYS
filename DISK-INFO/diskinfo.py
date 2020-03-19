import psutil

print("")
print("disks / partitions.")
print("")
drive = psutil.disk_partitions()
print(drive)

print("")
print("disk usage.")
print("")
gebruik = psutil.disk_usage('/')
print(gebruik)

print("")
print("read write.")
print("")
leesschrijf = psutil.disk_io_counters(perdisk=False)
print(leesschrijf)
