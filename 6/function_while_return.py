def get_formated_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print('\n Please tell me your name：')
    print("(enter 'q' at any time to quit)")
    f_name = input('Fist name：')
    if f_name == 'q':
        break

    l_name = input('Last name：')
    if l_name == 'q':
        break

    formated_name = get_formated_name(f_name, l_name)
    print(f'Hello，{formated_name}')
