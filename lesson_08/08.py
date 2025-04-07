def sum_of_numbers():
    """
    the function calculate elements in the list_of_numbers
    :return:
    """
    try:
        result = []
        for item in list_of_numbers:
            # print(item)
            try:
                result.append(sum(int(num) for num in item.split(',')))
            # finally:
            #     print("Go home, everthing works!!!")
            except ValueError:
                result.append("Не можу це зробити")
        print(result)
    except TypeError as error:
        print(f"Error is displayed: {error}")
    finally:
        print("Go home, everthing works!!!")


list_of_numbers = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']
sum_of_numbers()