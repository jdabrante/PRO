def count_name(name_list: list, count=0)-> int:
    text = name_list[0].replace(" ","")
    count += len(text)
    if len(name_list) == 1:
        return count
    return count_name(name_list[1:], count)

names = ["Yo soy María","Yo soy Pepa","Yo no soy Josefina"]

total = count_name(names)
print(total)