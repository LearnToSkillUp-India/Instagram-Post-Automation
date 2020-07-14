# Instagram-Post-Automation
Automate the creation of posts on Instagram.

The script is designed for a grid of 9 posts. Thus post numbers will be from 1 to 9. There are 2 modes - **single** posts and **slider** posts.

On every itieration, post number, mode and slider number is displayed.

After selecting modes, there are 3 options:
1. Slide having only text
2. Slide having only image
3. Slide haing both text and image

The text and image path has to be pasted as it is.

For slides having images, you can continue to make changes with the image and scale it as required. 

Similarly for slides having text, you can continue to make changes for maximum number characters in a line.

For length of the pipes, there is a safety number that will ensure the pipes don't overlap over text/image. But if you want to increase/decrease size of the pipes, you can specify offset as a list.
[top, bottom, left, right]

For example, [0 60 -60 0] will **increase bottom pipe** length by 60 px and **decrease left pipe** length by 60px.

Keep offset as [0 0 0 0] as default.

The posts will be saved accordingly till the count reaches the number of slides to be made in that post.

Remaining work:
- [ ] Save posts by adding post title and by creating a folder
- [ ] Automatically increase offset for special cases
- [ ] Automatically upload to drive after confirmation from user
