from typing import Never

class NumberUtilities:
    @staticmethod
    def get_ordinal_string(n):
        '''
        Convert an integer into its ordinal representation::

            get_ordinal_string(0)   => '0th'
            get_ordinal_string(3)   => '3rd'
            get_ordinal_string(122) => '122nd'
            get_ordinal_string(213) => '213th'
        '''
        n = int(n)
        if 11 <= (n % 100) <= 13:
            suffix = 'th'
        else:
            suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
        return str(n) + suffix