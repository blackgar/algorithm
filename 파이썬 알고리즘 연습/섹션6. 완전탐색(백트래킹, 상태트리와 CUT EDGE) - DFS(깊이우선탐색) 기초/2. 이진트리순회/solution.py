import sys

sys.stdin = open("input.txt")

def jun_wui(x):
    if x > 7:
        return
    else:
        print(x, end=" ")
        jun_wui(x * 2)
        jun_wui(x * 2 + 1)
def joong_wui(x):
    if x > 7:
        return
    else:
        joong_wui(x*2)
        print(x, end=" ")
        joong_wui(x*2+1)
def hoo_wui(x):
    if x > 7:
        return
    else:
        hoo_wui(x * 2)
        hoo_wui(x * 2 + 1)
        print(x, end=" ")


jun_wui(1)
print("전위")

joong_wui(1)
print("중위")

hoo_wui(1)
print("후위")