import tkinter as tk

'''
    Much of this code was elucidated by Bryan Oakley on StackOverflow.com. 
    Without his explanations and examples, I would not have figured out how to 
    create a configurable Tkinter scrollbar. Any mistakes in this code are mine 
    of course.

    I didn't add the little arrows at the ends of the trough.
'''

class Scrollbar(tk.Canvas):
    '''
        A scrollbar is gridded as a sibling of what it's scrolling.
    '''

    def __init__(self, parent, orient='vertical', hideable=False, **kwargs):
        print('kwargs is', kwargs)

        '''
            kwargs is {
                'width': 17, 
                'command': <bound method YView.yview of 
                    <widgets.Text object .!canvas.!frame.!frame.!text>>}

            https://stackoverflow.com/questions/15411107
            You can use dict.pop:... delete an item in a dictionary only if the given key exists... not certain if key exists in the dictionary...

                mydict.pop("key", None)

            ...if the second argument, None is not given, KeyError is raised if the key is not in the dictionary. Providing the second argument prevents the conditional exception... the second argument to .pop() is what it returns if the key is not found. 
        '''

        self.command = kwargs.pop('command', None)
        print('self.command is', self.command)
        tk.Canvas.__init__(self, parent, **kwargs)

        self.orient = orient
        self.hideable = hideable

        self.new_start_y = 0
        self.new_start_x = 0
        self.first_y = 0
        self.first_x = 0

        self.slidercolor = 'steelblue'
        self.troughcolor = 'lightgray'

        self.config(bg=self.troughcolor, bd=0, highlightthickness=0)

        # coordinates are irrelevant; they will be recomputed
        #   in the 'set' method
        self.create_rectangle(
            0, 0, 1, 1, 
            fill=self.slidercolor, 
            width=2, # this is border width
            outline='teal', 
            tags=('slider',))
        self.bind('<ButtonPress-1>', self.move_on_click)

        self.bind('<ButtonPress-1>', self.start_scroll, add='+')
        self.bind('<B1-Motion>', self.move_on_scroll)
        self.bind('<ButtonRelease-1>', self.end_scroll)

    def set(self, lo, hi):
        '''
            For resizing & repositioning the slider. The hideable
            scrollbar portion is by Fredrik Lundh, one of Tkinter's authors.
        '''

        lo = float(lo)
        hi = float(hi)

        if self.hideable is True:
            if lo <= 0.0 and hi >= 1.0:
                self.grid_remove()
                return
            else:
                self.grid()

        height = self.winfo_height()
        width = self.winfo_width()

        if self.orient == 'vertical':
            x0 = 2
            y0 = max(int(height * lo), 0)
            x1 = width - 2
            y1 = min(int(height * hi), height)
        # This was the tricky part of making a horizontal scrollbar 
        #   when I already knew how to make a vertical one.
        #   You can't just change all the "height" to "width"
        #   and "y" to "x". You also have to reverse what x0 etc 
        #   are equal to, comparing code in if and elif. Till that was
        #   done, everything worked but the horizontal scrollbar's 
        #   slider moved up & down.
        elif self.orient == 'horizontal':
            x0 = max(int(width * lo), 0)
            y0 = 2
            x1 = min(int(width * hi), width)
            y1 = height

        self.coords('slider', x0, y0, x1, y1)
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def move_on_click(self, event):
        if self.orient == 'vertical':
            # don't scroll on click if mouse pointer is w/in slider
            y = event.y / self.winfo_height()
            if event.y < self.y0 or event.y > self.y1:
                self.command('moveto', y)
            # get starting position of a scrolling event
            else:
                self.first_y = event.y
        elif self.orient == 'horizontal':
            # do nothing if mouse pointer is w/in slider
            x = event.x / self.winfo_width()
            if event.x < self.x0 or event.x > self.x1:
                self.command('moveto', x)
            # get starting position of a scrolling event
            else:
                self.first_x = event.x

    def start_scroll(self, event):
        if self.orient == 'vertical':
            self.last_y = event.y 
            self.y_move_on_click = int(event.y - self.coords('slider')[1])
        elif self.orient == 'horizontal':
            self.last_x = event.x 
            self.x_move_on_click = int(event.x - self.coords('slider')[0])

    def end_scroll(self, event):
        if self.orient == 'vertical':
            self.new_start_y = event.y
        elif self.orient == 'horizontal':
            self.new_start_x = event.x

    def move_on_scroll(self, event):

        # Only scroll if the mouse moves a few pixels. This makes
        #   the click-in-trough work right even if the click smears
        #   a little. Otherwise, a perfectly motionless mouse click
        #   is the only way to get the trough click to work right.
        #   Setting jerkiness to 5 or more makes very sloppy trough
        #   clicking work, but then scrolling is not smooth. 3 is OK.

        jerkiness = 3

        if self.orient == 'vertical':
            if abs(event.y - self.last_y) < jerkiness:
                return
            # scroll the scrolled widget in proportion to mouse motion
            #   compute whether scrolling up or down
            delta = 1 if event.y > self.last_y else -1
            #   remember this location for the next time this is called
            self.last_y = event.y
            #   do the scroll
            self.command('scroll', delta, 'units')
            # afix slider to mouse pointer
            mouse_pos = event.y - self.first_y
            if self.new_start_y != 0:
                mouse_pos = event.y - self.y_move_on_click
            self.command('moveto', mouse_pos/self.winfo_height()) 
        elif self.orient == 'horizontal':
            if abs(event.x - self.last_x) < jerkiness:
                return
            # scroll the scrolled widget in proportion to mouse motion
            #   compute whether scrolling left or right
            delta = 1 if event.x > self.last_x else -1
            #   remember this location for the next time this is called
            self.last_x = event.x
            #   do the scroll
            self.command('scroll', delta, 'units')
            # afix slider to mouse pointer
            mouse_pos = event.x - self.first_x
            if self.new_start_x != 0:
                mouse_pos = event.x - self.x_move_on_click
            self.command('moveto', mouse_pos/self.winfo_width()) 

    def colorize(self):
        print('colorize')
        self.slidercolor = 'blue'
        self.troughcolor = 'bisque'
        self.config(bg=self.troughcolor)

if __name__ == '__main__':

    def resize_scrollbar():
        root.update_idletasks()  
        canvas.config(scrollregion=canvas.bbox('all')) 

    def resize_window():
        root.update_idletasks()
        page_x = content.winfo_reqwidth()
        page_y = content.winfo_reqheight()
        root.geometry('{}x{}'.format(page_x, page_y))

    root = tk.Tk()
    root.config(bg='yellow')
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=0)

    canvas = tk.Canvas(root, bg='tan')
    canvas.grid(column=0, row=0, sticky='news')

    content = tk.Frame(canvas)
    content.grid_columnconfigure(0, weight=1)
    content.grid_rowconfigure(0, weight=1)

    ysb_canv = Scrollbar(root, width=24, hideable=True, command=canvas.yview)
    xsb_canv = Scrollbar(root, height=24, hideable=True, command=canvas.xview, orient='horizontal')
    canvas.config(yscrollcommand=ysb_canv.set, xscrollcommand=xsb_canv.set)

    frame = tk.Frame(content)
    frame.grid_columnconfigure(0, weight=0)
    frame.grid_rowconfigure(0, weight=1)

    text = tk.Text(frame, bd=0)
    ysb_txt = Scrollbar(frame, width=17, command=text.yview)

    text.config(yscrollcommand=ysb_txt.set)

    space = tk.Frame(content, width=1200, height=500)

    ysb_canv.grid(column=1, row=0, sticky='ns')
    xsb_canv.grid(column=0, row=1, sticky='ew')
    frame.grid(column=0, row=0, sticky='news')
    text.grid(column=0, row=0)
    ysb_txt.grid(column=1, row=0, sticky='ns')
    space.grid(column=0, row=1)

    with open(__file__, 'r') as f:
        text.insert('end', f.read())

    canvas.create_window(0, 0, anchor='nw', window=content)

    resize_scrollbar()
    resize_window()

    root.mainloop()