class Solution:
    def romanToInt(self, s: str) -> int:
        general_list = {}
        general_list['I'] = 1
        general_list['V'] = 5
        general_list['X'] = 10
        general_list['L'] = 50
        general_list['C'] = 100
        general_list['D'] = 500
        general_list['M'] = 1000

        specific_dictionary = {}
        specific_dictionary['IV'] = 4
        specific_dictionary['IX'] = 9
        specific_dictionary['XL'] = 40
        specific_dictionary['XC'] = 90
        specific_dictionary['CD'] = 400
        specific_dictionary['CM'] = 900

        if s in specific_dictionary.keys():
            return specific_dictionary[s]
        else:
            sum = 0
            i = 0
            while i < int(len(s)):
                if i < int(len(s)) - 1 and general_list[s[i]] < general_list[s[i+1]]:
                    sum += specific_dictionary[s[i]+s[i+1]]
                    i += 1
                else:
                    sum += general_list[s[i]]
                i += 1
            return sum