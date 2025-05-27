class Text:
    def render(self) -> str:
        pass


class PlainText(Text):
    def __init__(self, content: str):
        self.content = content

    def render(self) -> str:
        return self.content


class TextDecorator(Text):
    def __init__(self, wrapped: Text):
        self.wrapped = wrapped

    def render(self) -> str:
        return self.wrapped.render()


class BoldDecorator(TextDecorator):
    def render(self) -> str:
        return f"<b>{super().render()}</b>"


class ItalicDecorator(TextDecorator):
    def render(self) -> str:
        return f"<i>{super().render()}</i>"


text = PlainText("Hello world!")
bold = BoldDecorator(text)
italic = ItalicDecorator(text)
print(f"Plain: {text.render()}")
print(f"Bold: {bold.render()}")
print(f"Plain: {italic.render()}")
