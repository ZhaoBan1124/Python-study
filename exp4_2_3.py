text="P@ssW0rd"
big_count = 0 #大写字母
small_count = 0 #小写字母
num_count = 0 #数字
other_count = 0 #其他字符

for i in text:
    if ord('A') <= ord(i) <= ord('Z'):
        big_count += 1
    elif ord('a') <= ord(i) <= ord('z'):
        small_count += 1
    elif ord('0') <= ord(i) <= ord('9'):
        num_count += 1
    else:
        other_count += 1

print(f"大写字母有{big_count}个")
print(f"小写字母有{small_count}个")
print(f"数字有{num_count}个")
print(f"其他字符有{other_count}个")