def is_palindromo(String):
    palindromo = String[::-1].lower()
    return String.lower() == palindromo

print(is_palindromo("Natan"))
