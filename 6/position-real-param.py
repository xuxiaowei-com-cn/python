def describe_pat(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pat('hamster', 'harry')
describe_pat('dog', 'willie')
