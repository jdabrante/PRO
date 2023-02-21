# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.
# Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

def rgb(r,g,b):
    d_rgb = [r,g,b]
    h_rgb = ""
    for d_code in d_rgb:
        if d_code > 255:
            d_code = f'{255:02x}'
        elif d_code < 0:
            d_code = f'{0:02x}'
        else: 
            d_code = f'{d_code:02x}'
        h_rgb += d_code
    return h_rgb.upper()
