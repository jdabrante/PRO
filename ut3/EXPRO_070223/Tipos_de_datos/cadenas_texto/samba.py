input = "//1.1.1.1/eoi/python"
clean_input = input.strip("/")
sidebar = clean_input.index("/")
ip = clean_input[:sidebar]
route = clean_input[sidebar:]
route
