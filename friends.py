
friends = ["Hatami", "Sarami", "Mohtadi", "Meshkati", "Karbaschian"]

print(friends)

friends.append("Amir Hossein")
print(friends)

friends[0], friends[2] = friends[2], friends[0]
print(friends)

friends.pop(-1)
print(friends)

#
# ۱- نام خود را به آرایه اضافه کرده و مجددا آن را print کنید.
#
# ۲- عضو اول و سوم آرایه را با هم جابه‌جا نمایید و سپس مجددا آن را print نمایید.
#
# ۳- نام خود را از آرایه پاک کنید و آن را print نمایید.
#
# توجه کنید همه مراحل باید به ترتیب و در یک کد اجرا شود. در مجموع ۴ مرتبه باید نتیجه تغییرات در آرایه print شوند.
