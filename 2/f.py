# f 字符串时 Python 3.6 引入的。
# Python 3.5 或更早的版本没需要使用 format() 方法

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(full_name)

print(f"{first_name.title()} {last_name}")

print("{} {}".format(first_name, last_name))
