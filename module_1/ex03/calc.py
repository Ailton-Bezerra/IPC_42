a = 42
b = -42

sum_result = a + b 
diff_result = a - b
prod_result = a * b
quot_result = int(a / b)

results = [sum_result, diff_result, prod_result, quot_result]
descriptions = ["Soma:", "Subtração:", "Produto:", "Divisão inteira:"]

for index in range(4):
    print(descriptions[index], results[index])