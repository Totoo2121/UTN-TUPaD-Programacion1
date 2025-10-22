def palindrome(palabra):
    if len(palabra) <= 1:
        return True      
    if palabra[0] != palabra[-1]:
        return False
    return palindrome(palabra[1:-1])     
print(palindrome("ana"))
print(palindrome("python"))