'''    ROMAN TO INTEGER   '''

dict_alignment = {  'I' : 1,  'V' : 5,
                    'X' : 10, 'L' : 50,
                    'C' : 100,'D' : 500,
                    'M' : 1000}        

def convert_to_int(roman_numeral, dict = dict_alignment):
    sum = 0
    len_of_numeral = len(roman_numeral)

    for ind in range(len_of_numeral): 
        if type(roman_numeral[ind]) != str:
            text = f'An invalid Roman numeral was supplied` {roman_numeral}'
            sum = 0
            break
        if ind == len_of_numeral-1:
            sum += dict[roman_numeral[ind]]
        elif dict[roman_numeral[ind]] >= dict[roman_numeral[ind+1]]:
            sum += dict[roman_numeral[ind]]
        else:
            sum -= dict[roman_numeral[ind]]            

    if sum:
        text = f'roman_numeral {roman_numeral} = {sum}'
    return   text

roman_numeral = 'MCMXCIV'
text = convert_to_int(roman_numeral)
print(text)