files_name = ['./io/dira/1.txt', './io/dirb/2.txt', './io/dirc/3.txt']

files_data = []

for f_name in files_name:
    with open(f_name) as f:
        files_data.append(f.read())

with open('./io/demo1.txt', mode='w') as f:
    for f_data in files_data:
        f.write(f_data)