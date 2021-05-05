# 有默认值的参数放在最后

def get_formated_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formated_name('jimi', 'hendrix')
print(musician)

musician = get_formated_name('john', 'lee', 'hooker')
print(musician)
