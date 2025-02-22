# Binary Calculator Script

class BaseTwoBinary:
    @staticmethod
    def decimal_to_binary(decimal:float):
        """
        Function to convert a decimal to a binary

        :param decimal: float value that will be converted
        :return: binary value of the binary converted
        """
        binary_value =  bin(int(decimal))[2:]
        if len(str(binary_value)) < 8:
            binary_value = '0'*(8-len(str(binary_value))) + binary_value
        return binary_value
    
    @staticmethod
    def binary_to_decimal(binary:str):
        """
        Function to convert a binary value to decimal

        :param binary: str value of the decimal that will be converted
        :return: int value that will be converted to binary
        """
        decimal = int(binary, 2)
        return decimal
    
    @staticmethod
    def full_binary_calculator(provided_type:str, value:float):
        """
        Function to convert a decimal to binary or binary to decimal
        
        :param provided_type: str value that will be converted
        :param value: float value that will be converted
        :return: str value of the binary converted
        """
        if provided_type == 'dec':
            y = BaseTwoBinary.decimal_to_binary(value)
            return f"The Binary of {value}: {y}"
        elif provided_type == 'bin':
            x = BaseTwoBinary.binary_to_decimal(value)
            return f"The Decimal of {value}: {x}"
        else:
            return "Invalid type. Please enter 'dec' or 'bin'"