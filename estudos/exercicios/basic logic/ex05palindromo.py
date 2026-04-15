def isPalindromo(String):
    palindromo = String[::-1].lower()
    return String.lower() == palindromo

print(isPalindromo("Natan"))
