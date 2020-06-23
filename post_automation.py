"""
Script Author: Saurabh S. Fegade
Script Purpose: To automate Instagram Post Design and Creation for Learn To Skill Up
"""
import sys
import PIL
from PIL import Image, ImageDraw, ImageFont
import textwrap

def DrawShapeTop(color, position, safety_number, offset):                   #function to draw top pipe
    if position == 'left':
        top_x1 = 135
        top_x2 = 243
    elif position == 'right':
        top_x1 = 863
        top_x2 = 971
    #top_y2 = 200
    top_y2 = 136 + safety_number + offset                                   #variable for adjusting height of pipe (136 default)
    rect = [(top_x1,0),(top_x2,top_y2)]
    draw.rectangle(rect, color, color)
    draw.ellipse([(top_x1, top_y2-52),(top_x2+1, top_y2+52)], color, color) #top_x2 + 1 for circle to touch rectangle properly; 52 is circle radius

def DrawShapeBottom(color, position, safety_number, offset):                #function to draw bottom pipe
    if position == 'left':
        bottom_x1 = 135
        bottom_x2 = 243
    elif position == 'right':
        bottom_x1 = 863
        bottom_x2 = 971
    bottom_y1 = 136 + safety_number + offset
    rect = [(bottom_x1, h-bottom_y1),(bottom_x2, h)]
    draw.rectangle(rect, color, color)
    draw.ellipse([(bottom_x1, h-bottom_y1-52),(bottom_x2+1, h-bottom_y1+52)], color, color)

def DrawShapeLeft(color, position, safety_number, offset):                  #function to draw left pipe
    if position == 'top':
        left_y1 = 54
        left_y2 = 162
    elif position == 'bottom':
        left_y1 = 863
        left_y2 = 971
    left_x2 = 136 + safety_number + offset
    rect = [(0, left_y1),(left_x2, left_y2)]
    draw.rectangle(rect, color, color)
    draw.ellipse([(left_x2-52, left_y1),(left_x2+52, left_y2+1)], color, color)

def DrawShapeRight(color, position, safety_number, offset):                 #function to draw right pipe
    if position == 'top':
        right_y1 = 54
        right_y2 = 162
    elif position == 'bottom':
        right_y1 = 863
        right_y2 = 971
    right_x1 = 136 + safety_number + offset
    rect = [(w-right_x1, right_y1),(w, right_y2)]
    draw.rectangle(rect, color, color)
    draw.ellipse([(w-right_x1-52, right_y1),(w-right_x1+52, right_y2+1)], color, color)

def DrawHashtag():                                                      #function to draw hashtag
    font = ImageFont.truetype('Open_Sans/OpenSans-Light.ttf', 40)  
    hashtag = '#learntoskillup'
    w1,h1 = draw.textsize(hashtag, font=font)
    #print(w1,h1)
    draw.text((((w-w1)/2), h-1.3*h1), hashtag, fill='black', font = font)  #1.3*h1 to shift hashtag up

def DrawCustomText():                                                   #function for taking custom input text with newlines
    font = ImageFont.truetype('Open_Sans/OpenSans-Bold.ttf',40)
    text = '''Lorem ipsum dolor sit amet,\npartem periculis an duo, eum lorem paulo an,\nmazim feugiat lobortis sea ut. 
    In est error eirmod vituperata, prima iudicabit rationibus mel et.'''
    w2, h2 = draw.multiline_textsize(text, font, spacing=4)
    print(w2,h2)
    draw.text((100,400), text, fill='grey', font = font)

def Draw_multiple_line_text(text, font_used, text_color, linespace, text_wrap_number):    #function to automatically drar text with wordwrap
    font = font_used
    lines = textwrap.wrap(text, width=text_wrap_number)                        #textwrap method to automatically shift words to newline if crowded
    width_list, height_list = [],[]
    for line in lines:                                                         #for loop to get width and height of each line and store it in lists
        line_width, line_height = font.getsize(line)
        width_list.append(line_width)
        height_list.append(line_height)
    max_width_line = max(width_list)                                           #line with max width for bounding box  
    max_height_line = max(height_list)                                         #line with max height for shifting next line with appropriate height 
    y_text = (max_height_line + linespace) * len(lines)                        #our bounding box for text would be of length 'max_width_line' and height 'y_text'
    #print(max_width_line, y_text)
    x_text1 = (w - max_width_line) / 2                                         #new calculated coordinates for text
    y_text1 = (h - y_text) / 2
    for line in lines:
        draw.text((x_text1, y_text1), 
                  line, font=font, fill=text_color)
        y_text1 += max_height_line+linespace
    return(max_width_line, y_text, width_list, height_list)                    #return following values to work outside function

def Add_image_to_template(image_path):                                                  #function to paste an image to template
    basewidth = 730
    image = Image.open(image_path)
    wpercent = (basewidth/float(image.size[0]))
    hsize = int((float(image.size[1])*float(wpercent)))
    img = image.resize((basewidth,hsize), Image.ANTIALIAS)
    #img = PIL.Image.new(mode = "RGB", size = (730, 670), color = (0, 0, 0))
    im.paste(img,(150,300))

def gets(msg, *types):                                                                  #modified input method for variable arguments
    return tuple([types[i](val) for i, val in enumerate(input(msg).split(' '))])

def draw_pipes(func_list, example_list, number):                                        #function to draw pipes according to the need
    for f in func_list:
        temp_dict = example_list[number-1]                                              #number would be different for each instance
        f(*temp_dict['{}'.format(f.__name__)])                                          #*args to pass list parameters


red, yellow, blue = 'rgb(246, 79, 89)', 'rgb(255, 189, 74)', 'rgb(82, 113, 255)'      
offset_list = []
msg = "Enter Post Number, Mode (slider/single) and number of slider posts\n(Example '3 slider 8' or '3 single 1')\n"
post_number, mode, slider_number = gets(msg, int, str, int)
if mode == 'single':
    count = 1
elif mode == 'slider':
    count = slider_number
else:
    print("Warning! Invalid mode.")
    sys.exit()
for i in range(0,count):
    print("[Post number : {}] --- [Mode : {}] --- [Slide: {}]".format(post_number, mode, i+1))
    keep_going = True
    while keep_going:
        image_or_text = int(input("\nPress '1' for adding text and '2' for adding image: "))    
        if image_or_text == 2:
            image_path = input("\nEnter Image Path: ")
            keep_going = False
        elif image_or_text == 1:
            text = input("\nEnter the text (Paste it directly): ")
            keep_going = False
        else:
            print("\nWarning! Enter valid choice.")
            keep_going = True
    keep_going1 = True
    while keep_going1:
        im = PIL.Image.new(mode = "RGB", size = (1080, 1080), color = (255, 255, 255))
        draw = ImageDraw.Draw(im)
        w,h = im.size
        #print(w,h)
        DrawHashtag()
        safety_number_width = 0                                                             #safety number is to reduce size of pipes if it overlaps with text
        safety_number_height = 0
        if image_or_text == 2:
            Add_image_to_template(image_path)
        elif image_or_text == 1:
            print("***\nMaximum number of characters in each line. Recommended = 30 or 25***")
            text_wrap_number = int(input("\nEnter maximum number of characters in each line: "))
            if (i+1) == 1:
                font = ImageFont.truetype('Open_Sans/OpenSans-Bold.ttf',56)
            else:
                font = ImageFont.truetype('Open_Sans/OpenSans-Regular.ttf',56)
            text_width, text_height, width_list, height_list = Draw_multiple_line_text(text, font, 'grey', 10, text_wrap_number)
            #last_line = width_list[-1:][0]                                                 #for automatic increase of pipe length (remaining)
            if (w-text_width)/2 < 136:
                safety_number_width = (w-text_width)/2 - 136 - 60                           #-136 to account for +136 in function and -60 to shift back by 60 px
            if (h-text_height)/2 < 136:    
                safety_number_height = (h-text_height)/2 - 136 - 60     
        #text1 = "The vehicle of Infineon’s logistics partner Kühne+Nagel will drive the distance between the factory premises and an external warehouse in the east of the city 4 times per working day."
        print("\n***Enter offset for top, bottom, left, right as a list: [top, bottom, left, right]\n\nExample: 60 0 -60 0 will give offset of 60 for top and -60 for left pipe.***\n")
        offset_list = [int(item) for item in input("Enter the list items : ").split()] 

        if (i+1) == 1:
            post1 = {'DrawShapeTop': [red, 'right', safety_number_height, offset_list[0]],           #usage of dictionaries to avoid redundancy using if...else
                     'DrawShapeBottom': [yellow, 'left', safety_number_height, offset_list[1]],      #for every different single and slider post
                     'DrawShapeLeft': [blue, 'top', safety_number_width, offset_list[2]]}
            
            post2 = {'DrawShapeTop': [blue, 'right', safety_number_height, offset_list[0]], 
                     'DrawShapeBottom': [red, 'left', safety_number_height, offset_list[1]],
                     'DrawShapeRight': [yellow, 'bottom', safety_number_width, offset_list[3]]}
            
            post3 = {'DrawShapeTop': [blue, 'left', safety_number_height, offset_list[0]],
                     'DrawShapeBottom':[red, 'right', safety_number_height, offset_list[1]],
                     'DrawShapeLeft': [yellow, 'bottom', safety_number_width, offset_list[2]],
                     'DrawShapeRight': [yellow, 'top', safety_number_width, offset_list[3]]}
            
            post4 = {'DrawShapeTop': [yellow, 'left', safety_number_height, offset_list[0]],
                     'DrawShapeBottom': [blue, 'right', safety_number_height, offset_list[1]],
                     'DrawShapeLeft': [red, 'bottom', safety_number_width, offset_list[2]]}
            
            post5 = {'DrawShapeTop': [red, 'left', safety_number_height, offset_list[0]],
                     'DrawShapeBottom': [yellow, 'left', safety_number_height, offset_list[1]],
                     'DrawShapeRight': [blue, 'top', safety_number_width, offset_list[3]]}
            
            post6 = {'DrawShapeTop': [red, 'right', safety_number_height, offset_list[0]],
                     'DrawShapeLeft': [blue, 'top', safety_number_width, offset_list[2]],
                     'DrawShapeRight': [yellow, 'bottom', safety_number_width, offset_list[3]]}
            
            post7 = {'DrawShapeTop': [blue, 'right', safety_number_height, offset_list[0]],
                     'DrawShapeBottom': [red, 'right', safety_number_height, offset_list[1]],
                     'DrawShapeLeft': [yellow, 'top', safety_number_width, offset_list[2]]}
            
            post8 = {'DrawShapeTop': [yellow, 'left', safety_number_height, offset_list[0]],
                     'DrawShapeBottom': [blue, 'right', safety_number_height, offset_list[1]],
                     'DrawShapeRight': [red, 'top', safety_number_width, offset_list[3]]}
            
            post9 = {'DrawShapeBottom': [blue, 'left', safety_number_height, offset_list[1]],
                     'DrawShapeLeft': [red, 'top', safety_number_width, offset_list[2]],
                     'DrawShapeRight': [yellow, 'bottom', safety_number_width, offset_list[3]]}
            post_list = [post1, post2, post3, post4, post5, post6, post7, post8, post9]
            
            post_func_dict = {'1': [DrawShapeTop, DrawShapeBottom, DrawShapeLeft],
                              '2': [DrawShapeTop, DrawShapeBottom, DrawShapeRight],
                              '3': [DrawShapeTop, DrawShapeBottom, DrawShapeLeft, DrawShapeRight],
                              '4': [DrawShapeTop, DrawShapeBottom, DrawShapeLeft],
                              '5': [DrawShapeTop, DrawShapeBottom, DrawShapeRight],
                              '6': [DrawShapeTop, DrawShapeLeft, DrawShapeRight],
                              '7': [DrawShapeTop, DrawShapeBottom, DrawShapeLeft],
                              '8': [DrawShapeTop, DrawShapeBottom, DrawShapeRight],
                              '9': [DrawShapeBottom, DrawShapeLeft, DrawShapeRight]}
            draw_pipes(post_func_dict['{}'.format(post_number)], post_list, post_number)
        
        elif (i+1) == 2: 
            color = yellow
            color1 = red
            position = 'bottom'
            if post_number == 3:
                color = yellow
                position = 'top'
            elif post_number == 5:
                color = blue
                position = 'top'
            elif post_number == 8:
                color = red
                color1 = yellow
                position = 'top'
                
            com_147_post2 = {'DrawShapeTop': [red, 'right', safety_number_height, offset_list[0]],         #com_147 because those posts will have same second post
                             'DrawShapeBottom': [yellow, 'left', safety_number_height, offset_list[1]],
                             'DrawShapeRight': [blue, 'bottom', safety_number_width, offset_list[3]]}
            com_235689_post2 = {'DrawShapeTop': [color1, 'right', safety_number_height, offset_list[0]],   #com_235689 because those posts will have same second post
                                'DrawShapeLeft': [color, position, safety_number_width, offset_list[2]],
                                'DrawShapeRight': [blue, 'bottom', safety_number_width, offset_list[3]]}
            com_post2_list = [com_147_post2, com_235689_post2]
            
            com_post2_func_dict = {'1': [DrawShapeTop, DrawShapeBottom, DrawShapeRight],
                                   '2': [DrawShapeTop, DrawShapeLeft, DrawShapeRight]}
            if post_number == (1 or 4 or 7):
                number = 1
            else:
                number = 2
            draw_pipes(com_post2_func_dict['{}'.format(number)], com_post2_list, number)
        
        else:
            com_post3 = {'DrawShapeTop': [red, 'left', safety_number_height, offset_list[0]],
                         'DrawShapeLeft': [blue, 'bottom', safety_number_width, offset_list[2]],
                         'DrawShapeRight': [yellow, 'top', safety_number_width, offset_list[3]]}
            
            com_post4 = {'DrawShapeBottom':[blue, 'left', safety_number_height, offset_list[1]],
                         'DrawShapeLeft': [yellow, 'top', safety_number_width, offset_list[2]],
                         'DrawShapeRight': [red, 'bottom', safety_number_width, offset_list[3]]}

            com_post5 = {'DrawShapeTop': [yellow, 'left', safety_number_height, offset_list[0]],
                         'DrawShapeLeft': [red, 'bottom', safety_number_width, offset_list[2]],
                         'DrawShapeRight': [blue, 'top', safety_number_width, offset_list[3]]}

            com_post6 = {'DrawShapeBottom':[red, 'left', safety_number_height, offset_list[1]],
                         'DrawShapeLeft': [blue, 'top', safety_number_width, offset_list[2]],
                         'DrawShapeRight': [yellow, 'bottom', safety_number_width, offset_list[3]]}

            com_post7 = {'DrawShapeTop': [blue, 'left', safety_number_height, offset_list[0]],
                         'DrawShapeLeft': [yellow, 'bottom', safety_number_width, offset_list[2]],
                         'DrawShapeRight': [red, 'top', safety_number_width, offset_list[3]]}

            com_post8 = {'DrawShapeBottom':[yellow, 'left', safety_number_height, offset_list[1]],
                         'DrawShapeLeft': [red, 'top', safety_number_width, offset_list[2]],
                         'DrawShapeRight': [blue, 'bottom', safety_number_width, offset_list[3]]}

            com_post9 = {'DrawShapeTop': [red, 'left', safety_number_height, offset_list[0]],
                         'DrawShapeLeft': [blue, 'bottom', safety_number_width, offset_list[2]],
                         'DrawShapeRight': [yellow, 'top', safety_number_width, offset_list[3]]}

            com_post10 = {'DrawShapeTop': [blue, 'right', safety_number_height, offset_list[0]],
                          'DrawShapeBottom': [red, 'right', safety_number_height, offset_list[1]],
                          'DrawShapeLeft': [yellow, 'top', safety_number_width, offset_list[2]]}
            com_post3_list = [com_post3, com_post4, com_post5, com_post6, com_post7, com_post8, com_post9, com_post10]

            com_post3_func_dict = {'3': [DrawShapeTop, DrawShapeLeft, DrawShapeRight],
                                   '4': [DrawShapeBottom, DrawShapeLeft, DrawShapeRight],
                                   '5': [DrawShapeTop, DrawShapeLeft, DrawShapeRight],
                                   '6': [DrawShapeBottom, DrawShapeLeft, DrawShapeRight],
                                   '7': [DrawShapeTop, DrawShapeLeft, DrawShapeRight],
                                   '8': [DrawShapeBottom, DrawShapeLeft, DrawShapeRight],
                                   '9': [DrawShapeTop, DrawShapeLeft, DrawShapeRight],
                                   '10': [DrawShapeTop, DrawShapeBottom, DrawShapeLeft]}
            draw_pipes(com_post3_func_dict['{}'.format(i+1)], com_post3_list, i+1-2)                #i+1-2 will make com_post3 list to start finding from index 0


        im.show()
        continue_input = input("\nDo you want to continue making changes? (y/n): ")
        if continue_input == 'Y' or continue_input == 'y':
            keep_going1 = True
        elif continue_input == 'N' or continue_input == 'n':
            keep_going1 = False
        else: 
            print("\n***Enter a valid response (Y/N)***")
            keep_going1 = True
    im.save('{}_{}.png'.format(post_number, i+1))

