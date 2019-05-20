import os

class Util:
    def getImagenOfFolder(self,folder):
        images = []
        absolutWay = os.path.abspath(folder)
        for currentFolder, subFolders, files  in os.walk(absolutWay):
            images.extend([os.path.join(currentFolder,file) for file in files if file.endswith('.png')])
        return images