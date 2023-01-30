def roman_to_arabic(roman_num):
    roman_dict = {'M': 1000, 'CM': 900, 'D': 500,
                  'CD': 400, 'C': 100, 'XC': 90,
                  'L': 50, 'XL': 40, 'X': 10,
                  'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    roman_num = roman_num.upper() + ' '  # Adds space to roman number and gets all symbols in uppercase
    letter_lst = []  # List of roman number letters
    for e in roman_num:
        letter_lst.append(e)
    roman_lst = []  # List of roman numbers
    for i in range(len(letter_lst)):
        if letter_lst[i] == 'M':
            roman_lst.append('M')
        elif letter_lst[i] == 'C' and letter_lst[i + 1] == 'M':
            roman_lst.append('CM')
            letter_lst[i + 1] = ''
        elif letter_lst[i] == 'D':
            roman_lst.append('D')
        elif letter_lst[i] == 'C' and letter_lst[i + 1] == 'D':
            roman_lst.append('CD')
            letter_lst[i + 1] = ''
        elif letter_lst[i] == 'C':
            roman_lst.append('C')
        elif letter_lst[i] == 'X' and letter_lst[i + 1] == 'C':
            roman_lst.append('XC')
            letter_lst[i + 1] = ''
        elif letter_lst[i] == 'L':
            roman_lst.append('L')
        elif letter_lst[i] == 'X' and letter_lst[i + 1] == 'L':
            roman_lst.append('XL')
            letter_lst[i + 1] = ''
        elif letter_lst[i] == 'X':
            roman_lst.append('X')
        elif letter_lst[i] == 'I' and letter_lst[i + 1] == 'X':
            roman_lst.append('IX')
            letter_lst[i + 1] = ''
        elif letter_lst[i] == 'V':
            roman_lst.append('V')
        elif letter_lst[i] == 'I' and letter_lst[i + 1] == 'V':
            roman_lst.append('IV')
            letter_lst[i + 1] = ''
        elif letter_lst[i] == 'I':
            roman_lst.append('I')
    valid_symbols = []  # List of valid symbols
    for k in roman_dict.keys():
        valid_symbols.append(k)  # Adds all keys from roman_dict dictionary
    unexpected_symbol_count = 0  # Unexpected symbol count
    for letter in roman_num:
        if letter not in valid_symbols:
            unexpected_symbol_count += 1
    arabic_lst = []  # List of arabic numbers
    if unexpected_symbol_count > 1:
        print('You entered wrong roman number!')
    else:
        for e in roman_lst:
            arabic_lst.append(roman_dict[e])
        print(sum(arabic_lst))  # Prints sum of arabic symbols


roman_to_arabic('McmlXIi')
