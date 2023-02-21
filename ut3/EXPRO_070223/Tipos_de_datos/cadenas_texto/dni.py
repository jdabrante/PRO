dni = "12345678"
letters ="TRWAGMYFPDXBNJZSQVHLCKE"
remainder = int(dni)%23
full_dni = f"{dni}{letters[remainder]}"
full_dni