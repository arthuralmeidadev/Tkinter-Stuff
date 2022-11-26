from tkinter import *


class ScrollableText:
    """
    EASY SCROLLED TKINTER TEXT THAT STAYS CONSISTENT INSIDE WIDGETS LIKE PANE WINDOWS

    -If there are multiple of these that must be next to each other, it is recommended that they are all inside a frame
     positioned with grid. To expand it to the edges, on the parent frame, use the methods:
     grid_rowconfigure(0, weight=1)
     grid_columnconfigure(1, weight=1)

     By: arthuralmeidadev (GitHub)
    """
    def __init__(self, master, wrap=None, label_frame=False):
        if label_frame is False:
            self.frame = Frame(master)
        else:
            self.frame = LabelFrame(master)
        # The conditional above selects the frame type

        self.frame.grid_rowconfigure(0, weight=1)                           # Row 0 takes priority
        self.frame.grid_columnconfigure(0, weight=1)                        # Column 0 takes priority
        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL)             # Creates main scrollbar
        self.base_scrollbar = Scrollbar(self.frame, orient=HORIZONTAL)      # Horizontal scrollbar for unwrapped texts
        self.scrollbar.grid(row=0, column=1, sticky=NS)                     # Places main scrollbar

        # This conditional below looks for the necessity to use the horizontal scrollbar, in case the text is unwrapped
        if wrap is not None:
            self.text = Text(self.frame, yscrollcommand=self.scrollbar.set)         # Creates the text field
        else:
            # noinspection PyTypeChecker
            self.text = Text(self.frame, yscrollcommand=self.scrollbar.set,         # Creates the text field
                             xscrollcommand=self.base_scrollbar.set, wrap=wrap)

            self.scrollbar.grid_configure(columnspan=2)             # Extends the main scrollbar to the bottom
            self.base_scrollbar.grid(row=1, column=0, sticky=EW)    # Places the horizontal scrollbar
            self.base_scrollbar.config(command=self.text.xview)     # Hooks the horizontal scrollbar to the text field

        self.scrollbar.config(command=self.text.yview)              # Hooks the main scrollbar to the text field
        self.text.grid(row=0, column=0, sticky=NW+SE)               # Places the text field

    # Overrides Text object 'config'
    def config(self, *args):
        self.text.config(*args)

    # Overrides Text object 'configure'
    def configure(self, *args):
        self.text.config(*args)

    # Overrides the frame settings
    def frame(self):
        return self.frame
