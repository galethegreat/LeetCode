from abc import ABC, abstractmethod
class Blob(ABC):

    @abstractmethod
    def displayInfo(self) ->List[str]:
        pass

class File(Blob):

    def __init__(self, name, content=""):

        self.name = name
        self._content = content

    def displayInfo(self):
        return [self.name]

    @property
    def content(self):

        return self._content

    @content.setter
    def content(self, content):

        self._content += content


class Folder(Blob):

    def __init__(self, name):

        self.name = name
        self.contents = {}

    def displayInfo(self):
        return sorted([val.name for val in self.contents.values()])

    def addBlob(self, blob):

        self.contents[blob.name] = blob


class FileSystem:

    def __init__(self):

        self.main = Folder('$')

        main_folder = Folder('')
        self.main.addBlob(main_folder)

    def _path_to_folders(self, path):

        if path == '/':
            return ['']

        return path.split('/')

    #@staticmethod
    def createFile(self, file_name, content, fileType):
        return fileType(file_name, content)

    def ls(self, path: str) -> List[str]:

        main = self.main
        folders = self._path_to_folders(path)

        for blob in folders:
            main = main.contents[blob]

        return main.displayInfo()

    def _createPath(self, folders):

        main = self.main

        for folder_name in folders:

            if folder_name in main.contents:

                main = main.contents[folder_name]

            else:
                new_folder = Folder(folder_name)

                main.addBlob(new_folder)
                main = main.contents[folder_name]

        return main


    def mkdir(self, path: str) -> None:
        folders = self._path_to_folders(path)
        self._createPath(folders)


    def addContentToFile(self, filePath: str, content: str) -> None:

        *folders, file_name = self._path_to_folders(filePath)

        dest_folder = self._createPath(folders)

        if file_name not in dest_folder.contents:
            file = File(file_name, content)

            dest_folder.addBlob(file)
        else:
            dest_folder.contents[file_name].content = content


    def readContentFromFile(self, filePath: str) -> str:
        main = self.main
        path = self._path_to_folders(filePath)

        for blob in path:

            main = main.contents[blob]

        return main.content
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
