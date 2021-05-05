# 有时候，需要接受任意数量的实参，但预先不知道传递参数给函数的会是什么样的信息
# 可将函数编编写成能够接受任意数量的键值对

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', fueld='physics')
print(user_profile)
