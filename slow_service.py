import time

for remaining in range(10, 0, -1):
    print("{:2d} seconds remaining.".format(remaining))
    time.sleep(1)

print("\rComplete!\n")