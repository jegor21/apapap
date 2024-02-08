def alfa(name):
    
    russian = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7, 'ж': 8, 'з': 9, 
                        'и': 1, 'й': 2, 'к': 3, 'л': 4, 'м': 5, 'н': 6, 'о': 7, 'п': 8, 'р': 9, 
                        'с': 1, 'т': 2, 'у': 3, 'ф': 4, 'х': 5, 'ц': 6, 'ч': 7, 'ш': 8, 'щ': 9, 
                        'ъ': 0, 'ы': 0, 'ь': 0, 'э': 0, 'ю': 0, 'я': 0}
    english = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 
                        'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9, 
                        's': 1, 't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8}
    
    name = name.lower()
    
    alpha = russian if any(char in russian for char in name) else english
    
    name_number = sum(alpha.get(char, 0) for char in name)
    
    while name_number > 9:
        name_number = sum(int(digit) for digit in str(name_number))
    
    return name_number


name = input("Введите ваше имя: ")
name_number = alfa(name)
print(f"Число вашего имени: {name_number}")

