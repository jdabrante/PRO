def adn2arn (adn: str, arn: str= "")-> str:
    if len(adn) == 0:
        return ""
    if adn[0] == "T":
        arn += "U" + adn2arn(adn[1:], arn)
    else: 
        arn += adn[0] + adn2arn(adn[1:], arn)
    return arn
    
print(adn2arn('GCGCACTCTTCTTTGCTCTT'))