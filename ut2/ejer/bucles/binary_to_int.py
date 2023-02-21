BIN_N = "1101"
bin_size = len(BIN_N)
result = 0
for i in range(bin_size):
    # Cálculo del exponente
    exponent = bin_size - i - 1
    digit = int(BIN_N[i])
    partial_result = digit * 2**exponent
    result += partial_result
    print(exponent)
