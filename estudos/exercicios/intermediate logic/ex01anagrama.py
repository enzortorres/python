def isAnagram(string1: str, string2: str) -> bool:
    string1_clean = string1.replace(" ", "").lower()
    string2_clean = string2.replace(" ", "").lower()

    return sorted(string1_clean) == sorted(string2_clean)

print(isAnagram("Amor", "Roma"))
print(isAnagram("PeDra", "pErdA"))
