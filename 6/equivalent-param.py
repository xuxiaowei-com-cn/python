def describe_pat(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


# 一条名为 Willie 的小狗
describe_pat('willie')
describe_pat(pet_name='willie')

# 一只名为 Harry 的仓鼠
describe_pat('harry', 'hamster')
describe_pat('harry', animal_type='hamster')
describe_pat(pet_name='harry', animal_type='hamster')
describe_pat(animal_type='hamster', pet_name='harry')
