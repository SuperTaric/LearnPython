with open('./io/dira/1.txt') as fa:
    file_data_1 = fa.read()

with open('./io/dirb/2.txt') as fb:
    file_data_2 = fb.read()

with open('./io/dirc/3.txt') as fc:
    file_data_3 = fc.read()

with open('./io/demo.txt', mode='w') as fd:
    fd.write(file_data_1)
    fd.write(file_data_2)
    fd.write(file_data_3)