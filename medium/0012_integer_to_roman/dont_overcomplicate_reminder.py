class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        roman = ''
        step = 2
        divider = 1000
        while num != 0:
            if str(num)[0] == '9' and num > 9:
                roman = roman + romans[divider//step] + romans[divider//step*10]
                divider = divider // step
                num = int(str(num)[1:])
            elif str(num)[0] == '9' and num == 9:
                roman += 'IX'
                return roman
            elif num // divider != 4 and num // divider != 9:
                roman += (num // divider)*romans[divider]
                num = num - (num // divider) * divider
            elif num // divider == 4:
                if num == 4:
                    roman += 'IV'
                    return roman
                else:
                    roman = roman + romans[divider] + romans[(divider//step)*10]
                    print(roman)
                    print(step)
                    num = num - (num // divider) * divider



            divider = divider // step

            if step == 2:
                step = 5
            else:
                step = 2
        return roman