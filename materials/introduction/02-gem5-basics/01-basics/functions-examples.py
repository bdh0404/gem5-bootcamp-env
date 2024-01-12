def print_hello():
    print("Hello")

def function_1(input_list):
    n = len(input_list)
    for i in range(n):
        input_list[i] = 2 * input_list[i]

def function_2(input_list):
    new_list = input_list[:]
    n = len(new_list)
    for i in range(n):
        new_list[i] = 10000 * new_list[i]
    return new_list

def function_3(input_list, another_function):
    return another_function(input_list)

if __name__ == "__m5_main__":
    print("Calling print_hello()")
    print_hello()
    print()

    print("Calling function_1()")
    input1 = [1, 2, 3]
    print("Input before applying function_1():", input1)
    output1 = function_1(input1)
    print("Input after applying function_1():", input1)
    print("Output 1:", output1)
    print()

    print("Calling function_2()")
    input2 = [4, 5, 6]
    print("Input before applying function_2():", input2)
    output2 = function_2(input2)
    print("Input after applying function_2():", input2)
    print("Output 2:", output2)
    print()

    input3 = [7, 8, 9]
    fx = function_2
    output3 = function_3(input3, fx)
    print("Output 3 :", output3)