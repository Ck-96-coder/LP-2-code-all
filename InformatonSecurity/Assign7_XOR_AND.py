def and127(var):
    for i in range(len(var)):
        o = ord(var[i]) & 127
        print(f"{o} = {chr(o)}")

# print(ord("A"))

def xor127(var):

    for i in range(len(var)):
        p= ord(var[i]) ^ 127
        print(f"{p} = {chr(p)}")

if  __name__ == "__main__":
    user_input = input("Enter a string: ")
    print("AND127 Of Input String:")
    and127(user_input)
    print("\nXOR127 Of Input String:")
    xor127(user_input)