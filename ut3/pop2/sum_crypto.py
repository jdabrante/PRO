# ******************
# SUMA CRIPTOGRÁFICA
# ******************
from pathlib import Path


def run(crypto_path: Path) -> float:
    # TU CÓDIGO AQUÍ
    sum_cr = "output"
    crypto_codes = {
        "sd": "-",
        "vo": ".",
        "ax": "0",
        "gh": "1",
        "hj": "2",
        "uv": "3",
        "ws": "4",
        "pk": "5",
        "et": "6",
        "mc": "7",  
        "rh": "8",
        "wb": "9",
    }
    with open(crypto_path) as f:
        sum_cr = []
        for line in f:
            initial_index = 0
            end_index = 2
            code_list = []
            stripped_line = line.strip()
            for _ in stripped_line:
                code_list.append(stripped_line[initial_index:end_index])
                initial_index += 2
                end_index += 2
            decrypted_value = ""
            for code in code_list:
                if code in crypto_codes:
                    decrypted_value += crypto_codes[code]
            decrypted_value = float(decrypted_value)
            sum_cr.append(decrypted_value)
        sum_cr = sum(sum_cr)

    return sum_cr


if __name__ == "__main__":
    run("data/sum_crypto/data1.crypto")
