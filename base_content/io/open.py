# f = open('./io/demo_GBK.txt', mode='w', encoding='GBK')
# f.write("王福林")
# f.close()

f = open('./io/demo_GBK.txt', mode='r', encoding='GBK')
data = f.readlines()
print(data)
f.close()