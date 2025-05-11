from abc import ABC, abstractmethod


"""Let's say we have different types of Documents: PDFDocument, WordDocument, etc. we want to instantiate them without knowing their specific types."""


# Common Interface
class Document(ABC):
    @abstractmethod
    def render(self):
        pass


# Concrete Implementation
class PDFDocument(Document):
    def render(self):
        print("Rendering PDF document")


class WordDocument(Document):
    def render(self):
        print("Rendering Word document")


# Factory Method
class DocumentFactory:
    def create_document(self, type):
        if type == "pdf":
            return PDFDocument()
        elif type == "word":
            return WordDocument()
        else:
            raise ValueError("Unknown document type")


# Usage
factory = DocumentFactory()

doc1 = factory.create_document("pdf")
doc2 = factory.create_document("word")

doc1.render()
doc2.render()
