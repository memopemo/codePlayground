from PIL import Image
i = Image.open("preview.png")
sum = (0,0,0)
for x in range(0,i.width):
    for y in range(0,i.height):
        t = i.getpixel((x,y))
        sum = (sum[0]+t[0], sum[1]+t[1], sum[2]+t[2])

sum = (sum[0]/(i.width*i.height),sum[1]/(i.width*i.height), sum[2]/(i.width*i.height))

print(sum)