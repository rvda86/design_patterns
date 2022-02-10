from abc import ABC, abstractmethod

class Button(ABC):
    def __init__(self):
        pass

class DarkButton(Button):
    def __init__(self):
        print("a dark mode Button has been created")

class LightButton(Button):
    def __init__(self):
        print("a light mode Button has been created")

class ScrollBar(ABC):
    def __init__(self):
        pass

class DarkScrollBar(ScrollBar):
    def __init__(self):
        print("a dark mode ScrollBar has been created")

class LightScrollBar(ScrollBar):
    def __init__(self):
        print("a light mode ScrollBar has been created")

class InputField(ABC):
    def __init__(self):
        pass   

class DarkInputField(InputField):
    def __init__(self):
        print("a dark mode InputField has been created")

class LightInputField(InputField):
    def __init__(self):
        print("a light mode InputField has been created")


class WidgetFactory(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_scrollbar(self):
        pass

    @abstractmethod
    def create_input_field(self):
        pass

class DarkModeWidgetFactory(WidgetFactory):
    def create_button(self):
        return DarkButton()

    def create_scrollbar(self):
        return DarkScrollBar()

    def create_input_field(self):
        return DarkInputField()

class LightModeWidgetFactory(WidgetFactory):
    def create_button(self):
        return LightButton()

    def create_scrollbar(self):
        return LightScrollBar()

    def create_input_field(self):
        return LightInputField()

class GUI:
    def __init__(self, factory):
        self.factory = factory

    def create_button(self):
        return self.factory.create_button()

    def create_scrollbar(self):
        return self.factory.create_scrollbar()

    def create_input_field(self):
        return self.factory.create_input_field()

gui = GUI(DarkModeWidgetFactory())
gui.create_button()
gui.create_input_field()
gui.create_scrollbar()

gui = GUI(LightModeWidgetFactory())
gui.create_button()
gui.create_input_field()
gui.create_scrollbar()