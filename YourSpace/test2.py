
def encrypt_the_encrypted_data(data):
    jump = int(len(data)/10)
    if jump % 2 != 0:
        jump += 1
    mini_jump = int(jump/2)
    for i in range(0,len(data)-jump*2, jump):
        char = ord(data[i].to_bytes(2, 'big'))
        # data[i] = data[i+mini_jump]
        data = data[:i] + ord(data[i+mini_jump].to_bytes(2, 'big')) + data[i + 1:]
        # data[mini_jump] = num
        data = data[:mini_jump+i] + char + data[mini_jump + i + 1:]
    return data

def asafasd():
    filepath = "saved_img\\unknown-5.png"
    with open(filepath, "rb") as file:
        # read all file data
        data1 = file.read()
        print(data1[19285:19295])
    data2 = encrypt_the_encrypted_data(data1)
    data2 = encrypt_the_encrypted_data(data2)
    print(data2[19285:19295])
    if data1==data2:
        print(5)

data = b"asaf is cool"
data1 = encrypt_the_encrypted_data(data)
print(encrypt_the_encrypted_data(data1))