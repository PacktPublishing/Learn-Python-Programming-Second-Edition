
with open('write_x.txt', 'x') as fw:
    fw.write('Writing line 1')  # this succeeds


with open('write_x.txt', 'x') as fw:
    fw.write('Writing line 2')  # this fails
