# x, y, w, h = map(int, input().split())

# width = x
# if 2 * x > w:
#     width = abs(x - w)
    
# height = y
# if 2 * y > h:
#     height = abs(y - h)

# if width > height:
#     print(height)
# else:
#     print(width)

x,y,w,h = map(int,input().split())
check_min = [x-0,w-x,y-0,h-y]
print(min(check_min))