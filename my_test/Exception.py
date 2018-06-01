# try:
#    fileName=input("please input fileName")
#    open("%s.txt"%fileName)
# except FileNotFoundError:
#    print("%s.txt file not found"%fileName)

# try:
#    stu=1
#    print(stu)
# except NameError:
#    print("stu not define")
# try:
#     print(stu)
# except BaseException:
#     print("stu no define")


# try:
#     stu='Jack'
#     print(stu)
# except BaseException as msg:
#     print(msg)
# else:
#     print("stu is define")
# finally:
#     print("The end!")
# '''
#
def division(x,y):
    if y==0:
        raise ZeroDivisionError("Zero in not allow")
    return x/y
try:
    division(8,0)
except BaseException as msg:
    print(msg)
