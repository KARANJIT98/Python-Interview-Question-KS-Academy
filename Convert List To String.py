'''
Convert the below List To String

li=['hey','lets','learn','python','together']
output string = hey lets learn python together

hint:-  " ".join() -> to concatinate element of an iterable (list,tuple) -> string
'''


def funx(li):
    str=" ".join(li)
    return str


li = ['hey', 'lets', 'learn', 'python', 'together']


print(funx(li))