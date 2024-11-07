                # hex_string = "1A" #58
                # 
                # 
                # hex_integer = int(hex_string , 16)
                # 
                # binary_string = bin(hex_integer)
                # 
                # binary_string = binary_string[2:]
                # 
                # print (binary_string)


                #code is printing but the numbers arent right


hex_string = input("enter your hexadecimal number to convert to binary :")

hex_integer = int(hex_string , 16)
binary_string = bin(hex_integer)
binary_string = binary_string[2:]

print(binary_string)

