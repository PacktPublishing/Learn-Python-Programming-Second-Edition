import shutil
import os


BASE_PATH = 'ops_example'  # this will be our base path

# let's perform an initial cleanup just in case
if os.path.exists(BASE_PATH) and os.path.isdir(BASE_PATH):
    shutil.rmtree(BASE_PATH)


os.mkdir(BASE_PATH)

path_b = os.path.join(BASE_PATH, 'A', 'B')
path_c = os.path.join(BASE_PATH, 'A', 'C')
path_d = os.path.join(BASE_PATH, 'A', 'D')


os.makedirs(path_b)
os.makedirs(path_c)


# we add three files in `ops_example/A/B`
for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(os.path.join(path_b, filename), 'w') as stream:
        stream.write(f'Some content here in {filename}\n')


shutil.move(path_b, path_d)


# we can also rename files
shutil.move(
    os.path.join(path_d, 'ex1.txt'),
    os.path.join(path_d, 'ex1d.txt')
)

# now call $ tree ops_example
