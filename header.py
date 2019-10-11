from domain import test
read_data = []
fname = input('Enter filename...')
with open(fname, 'r+') as file:
    for value in file.readlines():
        print(value)
        status = test(value)
        read_data.append(status)
file.close()
