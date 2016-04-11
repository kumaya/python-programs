def decimalToRoman(dec, rom, decL, romL):
    if dec:
        if dec < decL[0]:
            return decimalToRoman(dec, rom, decL[1:], romL[1:])
        else:
            return decimalToRoman(dec-decL[0], rom+romL[0], decL, romL)
    return rom


if __name__ == "__main__":
    decL = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romL = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    dec = 1954
    rom = ''
    print ("Decimal representation: %d \nRoman representation: %s" %(dec,decimalToRoman(dec, rom, decL, romL)))