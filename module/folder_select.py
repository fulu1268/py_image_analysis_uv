# https://edusecrets.com/lesson-02-creating-a-file-select-button-in-jupyter-notebook/
import traitlets
from ipywidgets import widgets

# from IPython.display import display
from tkinter import Tk, filedialog


class SelectFolderButton(widgets.Button):
    
    """A file widget that leverages tkinter.filedialog."""

    def __init__(self):
        super(SelectFolderButton, self).__init__()
        
        # Add the selected_Folder trait
        self.add_traits(Folder=traitlets.traitlets.List())
        
        # Create the button.
        self.description = "Select Folder"
        
        self.icon = "square-o"
        self.style.button_color = "orange"
        # Set on click behavior.
        self.on_click(self.select_Folder)
        

    @staticmethod
    def select_Folder(b):
        
        """Generate instance of tkinter.filedialog.

        Parameters
        ----------
        b : obj:
            An instance of ipywidgets.widgets.Button 
        """
        # Create Tk root
        root = Tk()
        # Hide the main window
        root.withdraw()
        # Raise the root to the top of all windows.
        root.call("wm", "attributes", ".", "-topmost", True)
        # List of selected Folderwill be set to b.value
        
        b.dir = filedialog.askdirectory()
        

        b.description = "Folder Selected"
        b.icon = "check-square-o"
        b.style.button_color = "lightgreen"
