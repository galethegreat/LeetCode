from abc import ABC, abstractmethod

class FileReadOnlyError(Exception):
    pass

class Blob(ABC):

    @abstractmethod
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, new_name):
        pass

    @abstractmethod
    def displayInfo(self) -> List[str]:
        pass

class File(Blob):

    @abstractmethod
    def __init__(self, name: str, content="") -> None:
        super().__init__(name)
        self._content = content

    @property
    @abstractmethod
    def content(sel) -> Optional[str]:
        pass

    @content.setter
    @abstractmethod
    def content(self, content: Optional[str]) -> None:
        pass

class TextFile(File):

    def __init__(self, name: str, content="", isReadOnly=False) -> None:
        super().__init__(name, content)
        self.isReadOnly = isReadOnly

    def displayInfo(self) -> List[str]:
        return [self.name]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, content: str) -> None:
        if self.isReadOnly:
            raise FileReadOnlyError(f'TextFile {self.name} is read-only')

        self._content = content

    def append(self, content_to_append: str) -> None:
        if self.isReadOnly:
            raise FileReadOnlyError(f'TextFile {self.name} is read-only')

        self._content += content_to_append

class Folder(Blob):

    def __init__(self, name: str, metadata=None) -> None:
        super().__init__(name)
        self.contents = dict()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def displayInfo(self) -> List[str]:
        return sorted([val.name for val in self.contents.values()])

    def addBlob(self, blob) -> None:
        self.contents[blob.name] = blob

class FileSystem:

    def __init__(self) -> None:

        self.main = Folder('$')
        main_folder = Folder('')
        self.main.addBlob(main_folder)

    @classmethod
    def createBlob(cls, file_name: str, fileType: Blob, content: Optional[str]) -> Blob:

        return fileType(file_name, content)

    #@staticmethod instead of protected?
    def _path_to_folders(self, path):

        assert len(path) > 0, f"Empty path provided, path must contain at least '/'"

        if path == '/':
            return ['']

        return path.split('/')

    #@staticmethod instead of protected?
    def _createPath(self, folders):

        main = self.main

        for folder_name in folders:

            if folder_name in main.contents:
                main = main.contents[folder_name]

            else:
                new_folder = FileSystem().createBlob(folder_name, Folder, content=None)

                main.addBlob(new_folder)
                main = main.contents[folder_name]

        return main

    def ls(self, path: str) -> List[str]:

        main = self.main
        folders = self._path_to_folders(path)

        for blob in folders:
            main = main.contents[blob]

        return main.displayInfo()

    def mkdir(self, path: str) -> None:
        folders = self._path_to_folders(path)
        self._createPath(folders)


    def addContentToFile(self, filePath: str, content: str) -> None:

        *folders, file_name = self._path_to_folders(filePath)

        dest_folder = self._createPath(folders)

        if file_name not in dest_folder.contents:
            file = FileSystem().createBlob(file_name, TextFile, content)
            dest_folder.addBlob(file)

        else:
            dest_folder.contents[file_name].append(content)


    def readContentFromFile(self, filePath: str) -> str:
        main = self.main
        path = self._path_to_folders(filePath)

        for blob in path:

            main = main.contents[blob]

        return main.content
