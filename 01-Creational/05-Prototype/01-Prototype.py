import copy


class Document:
    def __init__(self, title, content, metadata=None):
        self.title = title
        self.content = content
        self.metadata = metadata or None

    def clone(self):
        # deep copy to avoid shared ref
        return copy.deepcopy(self)

    def __str__(self):
        return (
            f"Title: {self.title}\nContent: {self.content}\nMetadata: {self.metadata}"
        )


# usage
# Create a prototype document
template_doc = Document(
    "Template", "This is a standard template", {"author": "Admin", "version": 1}
)

# Clone it and modify
doc1 = template_doc.clone()
doc1.title = "Client Proposal"
doc1.metadata["author"] = "Alice"

doc2 = template_doc.clone()
doc2.title = "Internal Memo"
doc2.metadata["author"] = "Bob"

print(doc1)
print("\n" + "-" * 40 + "\n")
print(doc2)
