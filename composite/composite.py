from abc import ABC, abstractmethod

class Component(ABC):

    @abstractmethod
    def get_html():
        pass

# Composite 
class Element(Component):
    
    def __init__(self, element: str, children=[]):
        self.tag_open = f'<{element}>'
        self.tag_close = f'</{element}>'
        self.children = children

    def get_html(self):
        html = f'\n{self.tag_open}'
        for child in self.children:
            html += child.get_html()
        html += f'\n{self.tag_close}'
        return html

    def add(self, index: int, component: Component):
        self.children.insert(index, component) 

    def remove(self, index: int):
        del self.children[index]

# Leaf
class Text(Component):

    def __init__(self, text: str):
        self.text = text

    def get_html(self):
        return f'\n{self.text}'

title = Element('title', [Text("This is my website")])
head = Element('head', [title])
h1 = Element('h1', [Text("Lorem Ipsum")])
p_text = Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
p = Element('p', [p_text])
body = Element('body', [h1, p, p])
html = Element('html', [head, body])
body.remove(2)
h2 = Element('h2', [Text("de Finibus Bonorum et Malorum")])
body.add(2, h2)
p_text = Text("Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")
p = Element('p', [p_text])
body.add(3, p)

f = open("index.html", "w")
f.write(html.get_html())
f.close()