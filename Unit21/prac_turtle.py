import turtle as t
t.shape('turtle')

# square
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)

# square_loop
# for i in range(4):
#     t.forward(100)
#     t.right(90)

# pentagon_loop
# for i in range(5):
#     t.forward(100)
#     t.right(360/5)

# polygon
# n = int(input())
# for i in range(n):
#     t.forward(100)
#     t.right(360/n)

# red_hexagon
# n = 6
# t.color('red') # 펜의 색깔
# t.begin_fill() # 색칠할 영역 시작
# for i in range(n):
#     t.forward(100)
#     t.right(360/n)
# t.end_fill() # 색칠할 영역 끝

# one circle
# t.circle(120) # 반지름 120

# circles
# n=60 # 원을 60번 그림
# t.speed('fastest') # 거북이 속도 가장 빠르게
# for i in range(n):
#     t.circle(120)
#     t.right(360/n) # 오른쪽으로 6도 회전

# vortex
# t.speed('fastest')
# for i in range(300):
#     t.forward(i) # i만큼 앞으로 이동. 반복할 때마다 선이 길어짐
#     t.right(91) # 오른쪽으로 91도 회전

t.mainloop()