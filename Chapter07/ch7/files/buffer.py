import os


buff = bytearray(os.path.getsize('fear.txt'))


with open('fear.txt', 'rb') as f:
    f.readinto(buff)

half = len(buff) // 2
buff[:half] = buff[:half].upper()
buff[half:] = buff[half:].lower()

with open('fear_mod.txt', 'wb') as fw:
    fw.write(buff)
