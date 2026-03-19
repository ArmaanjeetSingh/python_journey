class Tag:
    def __init__(self,name,content = ""):
        self.name = name
        self.content = content

    def render(self):
        return f"<{self.name}>{self.content}</{self.name}>"


class Head(Tag):
    def __init__(self):
        super().__init__("head")
        self.children = []

    def add_tag(self, tag):
        self.children.append(tag)

    def render(self):#overrding render
        content = ""
        for child in self.children:
            content += child.render()
        return f"<head>{content}</head>"



class Body(Tag): #Body extends Tag
    def __init__(self):
        super().__init__("body")
        self.children = []

    def add_tag(self, tag):
        self.children.append(tag)

    def render(self):#overrding render
        content = ""
        for child in self.children:
            content += child.render()
        return f"<body>{content}</body>"

class HtmlDoc:
    def __init__(self):
        self.head = Head()
        self.body = Body()

    def add_tag(self,name,content):
        tag = Tag(name, content)
        self.body.add_tag(tag)

    def add_head_tag(self, name, content):
        self.head.add_tag(Tag(name, content))

    def render(self):
        return f"<html><head>{self.head.render()}</head><body>{self.body.render()}</body></html>"

doc = HtmlDoc()
doc.add_tag("h1", "Main Heading")
doc.add_tag("h2", "Subheading")
doc.add_tag("p", "This is a paragraph")

with open('html1.htm','w',encoding='utf-8',newline='') as htmlFile:
    print(doc.render(),file = htmlFile)
