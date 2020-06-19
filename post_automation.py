import PIL
from PIL import Image, ImageDraw, ImageFont
import textwrap

  
im = PIL.Image.new(mode = "RGB", size = (1080, 1080), color = (255, 255, 255))


draw = ImageDraw.Draw(im)
w,h = 1080,1080

def DrawShapeTop(color):
    rect = [(135,0),(243,136)]
    draw.rectangle(rect, color, color)
    draw.ellipse([(135,84),(244,193)], color, color)

def DrawShapeBottom(color):
    rect = [(135,h-136),(243,h)]
    draw.rectangle(rect, color, color)
    draw.ellipse([(135,h-136-52),(244,h-136+57)], color, color)

def DrawShapeLeft(color):
    rect = [(0,300),(136,408)]
    draw.rectangle(rect, color, color)
    draw.ellipse([(136-52,300),(136+57,409)], color, color)

def DrawShapeRight(color):
    rect = [(w-136,192),(w,300)]
    draw.rectangle(rect, color, color)
    draw.ellipse([(w-136-52,192),(w-136+57,301)], color, color)

def DrawHashtag():
    font = ImageFont.truetype('Open_Sans/OpenSans-Light.ttf', 40)  
    hashtag = '#learntoskillup'
    w1,h1 = draw.textsize(hashtag, font=font)
    #print(w1,h1)
    draw.text((((w-w1)/2), h-1.3*h1), hashtag, fill='black', font = font)

def DrawText():
    font = ImageFont.truetype('Open_Sans/OpenSans-Bold.ttf',40)
    text = '''Lorem ipsum dolor sit amet,\npartem periculis an duo, eum lorem paulo an,\nmazim feugiat lobortis sea ut. 
    In est error eirmod vituperata, prima iudicabit rationibus mel et.'''
    w2, h2 = draw.multiline_textsize(text, font, spacing=4)
    print(w2,h2)
    draw.text((100,400), text, fill='grey', font = font)

def Draw_multiple_line_text(text, text_color, linespace):
    #text_start_height = 0
    font = ImageFont.truetype('Open_Sans/OpenSans-Bold.ttf',56)
    #y_text = text_start_height
    lines = textwrap.wrap(text, width=30)
    print(len(lines))
    width_list, height_list = [],[]
    for line in lines:
        line_width, line_height = font.getsize(line)
        width_list.append(line_width)
        height_list.append(line_height)
    print(width_list)
    print(height_list)
    max_width_line = max(width_list)
    max_height_line = max(height_list)
    y_text = (max_height_line + linespace) * len(lines) # Our bounding box for text would be of length 'max_width_line' and height 'y_text'
    #print(y_text)
    x_text1 = (w - max_width_line) / 2
    y_text1 = (h - y_text) / 2
    print(x_text1,y_text1)
    for line in lines:
        line_width, line_height = font.getsize(line)
        #print(line_width,line_height)        
        draw.text((x_text1, y_text1), 
                  line, font=font, fill=text_color)
        y_text1 += max_height_line+linespace

def Add_image_to_template():
    basewidth = 730
    image = Image.open("cloud.png")
    wpercent = (basewidth/float(image.size[0]))
    hsize = int((float(image.size[1])*float(wpercent)))
    img = image.resize((basewidth,hsize), Image.ANTIALIAS)
    #img = PIL.Image.new(mode = "RGB", size = (730, 670), color = (0, 0, 0))
    im.paste(img,(150,300))


DrawShapeTop('rgb(82, 113, 255)')
DrawShapeBottom('rgb(246, 79, 89)')
#DrawShapeLeft('rgb(255, 189, 74)')
DrawShapeRight('rgb(255, 189, 74)')
DrawHashtag()
Add_image_to_template()

text2 = "The elections were conducted with the help of online security firm Kaspersky Labs and its blockchain enabled voting platform, Polys."
text1 = "The vehicle of Infineon’s logistics partner Kühne+Nagel will drive the distance between the factory premises and an external warehouse in the east of the city 4 times per working day."
#text_start_height = 100
#Draw_multiple_line_text(text2, 'grey',10)
#DrawText()


im.show()
#im.save('temp2.png')
'''mask = im.resize((w, h), Image.ANTIALIAS)
mask.show() 
mask.save('abc1.png')'''
