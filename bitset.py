class bitset:
    def to_binary(ascii_code: int, bit: int):
        m_binary = bin(ascii_code).replace('0b', '')
        reversed_m_binary = m_binary[::-1]
        while len(reversed_m_binary) < bit:
            reversed_m_binary += '0'
        m_binary = reversed_m_binary[::-1]
        return m_binary

    def to_text(binary: str):
        reversed_binary = binary[::-1]
        ascii_code = 0
        for bit_value, bit in enumerate(reversed_binary):
            two_n = pow(2, int(bit_value))
            ascii_code += two_n * int(bit)
        return chr(ascii_code)
