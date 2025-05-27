class FileReader:
    def __init__(self, filename):
        print(f"[FileReader] Loading file: {filename}")
        with open(filename, "r") as f:
            self.content = f.read()

    def get_content(self):
        return self.content


class FileReaderProxy:
    def __init__(self, filename):
        self.filename = filename
        self._real_reader = None

    def get_content(self):
        if self._real_reader is None:
            print("[Proxy] Lazy loading FileReader...")
            self._real_reader = FileReader(self.filename)
        return self._real_reader.get_content()


# Usage Example
if __name__ == "__main__":

    proxy = FileReaderProxy("sample.txt")
    print("Proxy created. File not yet loaded.")

    print("\nNow accessing content:")
    content = proxy.get_content()
    print("\nContent from file:")
    print(content)
