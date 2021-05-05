# 关键字实参是传递给函数的名称值对
# 全都使用关键字实参时，与键值顺序无关
# 混合使用时，位置实参必须放在前面，关键字实参必须放在后面，不可重复，不可穿插

def describe_pat(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pat(animal_type='hamster', pet_name='harry')
# 全都使用关键字实参时，与键值顺序无关
describe_pat(pet_name='harry', animal_type='hamster')

# 混合使用时，位置实参必须放在前面，关键字实参必须放在后面，不可重复，不可穿插
describe_pat('harry', pet_name='harry')

# 多次调用
describe_pat(animal_type='dog', pet_name='willie')
