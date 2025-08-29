red = "\033[1;41m"
pink = "\033[1;105m"
blue = "\033[1;44m"
reset = "\033[m"

first_name = ["Ailton", "Vinicius", "Thawan"]
last_name = ["Bezerra", "Kaique", "Pereira"]
colors = [red, pink, blue]

for index in range(3):
    print(colors[index], first_name[index], "\t" + last_name[index], reset, end = "\n")