




def encrypt_the_encrypted_data(data):
    jump = int(len(data)/10)
    if jump % 2 != 0:
        jump += 1
    mini_jump = int(jump/2)
    for i in range(0,len(data)-jump*2, jump):
        char = data[i]
        # data[i] = data[i+mini_jump]
        data = data[:i] + data[i+mini_jump] + data[i + 1:]
        # data[mini_jump] = num
        data = data[:mini_jump+i] + char + data[mini_jump + i + 1:]
    return data


filepath = "saved_img\\unknown-5.png"
with open(filepath, "rb") as file:
    # read all file data
    data = file.read()
    print(type(data))
# data = "asaf is cool"
new_data = encrypt_the_encrypted_data(data)
print(new_data)
new_data = encrypt_the_encrypted_data(new_data)
print(new_data)
with open(filepath, "wb") as file:
    file.write(new_data)

