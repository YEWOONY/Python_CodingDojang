path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
# temp = path.split('\\')
# filename = temp[-1]

# 더짧은코드
filename = path[path.rfind('\\')+1:]

print(filename)