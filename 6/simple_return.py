def get_formated_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formated_name('jimi', 'hendrix')
print(musician)
