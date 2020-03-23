#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# pylint: disable=too-many-ancestors
"""GUI for pdf_split."""

import tkinter as tk


class PdfSplitGUI(tk.Frame):
    """GUI for pdf_split."""

    def __init__(self, master=None):
        """Initialize the application."""
        super().__init__(master)
        self.master = master
        self.pack()
        # set up widgets
        self.create_widgets()

    def create_widgets(self):
        """Set up the widgets."""
        # create menu bar instance
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)
        # create file menu instance
        self.file = tk.Menu(self.menu)
        # add open command to file menu
        self.file.add_command(label="Open")
        # add file menu to menu bar
        self.menu.add_cascade(label="File", menu=self.file)


def pdf_split_gui():
    """Set up the application."""
    # create the window
    root = tk.Tk()
    # create the application
    app = PdfSplitGUI(root)
    # set the window title
    app.master.title("PDF Splitter GUI")
    # set window size
    app.master.geometry("720x480")
    # start the program
    app.mainloop()


if __name__ == "__main__":
    pdf_split_gui()
