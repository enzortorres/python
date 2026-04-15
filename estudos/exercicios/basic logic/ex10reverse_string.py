def reverse_splicing(string: str):
    return string[::-1]

def reverse_looping(string: str) -> str:
    string_reversed = ""
    for i in range(len(string)-1, -1, -1):
        string_reversed += string[i]
    return string_reversed

print(reverse_splicing("Enzo"))
print(reverse_looping("Enzo"))