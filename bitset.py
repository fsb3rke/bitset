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

m_input = input("Please enter char or ascii-code: ")
if type(m_input) is type(""):
    print(to_binary(ord(m_input), 8))
elif type(m_input) is type(0):
    print(to_binary(m_input, 8))

m_input = str(input("Please enter binary: "))
print(to_text(m_input))

m_input = input("Please enter text: ")
for i in m_input:
    print(to_binary(ord(i), 8))
