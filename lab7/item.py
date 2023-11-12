class Item():
    def __init__(self):
        self.__title = ""
        self.__playTime = 0
        self.__have = False
        self.__comment = ""
    def getTitle(self):
        return self.__title
    def getPlayTime(self):
        return self.__playTime
    def getHave(self):
        return self.__have
    def getComment(self):
        return self.__comment
    def setTitle(self, newTitle):
        self.__title = newTitle
    def setPlayTime(self, newPlayTime):
        self.__playTime = newPlayTime
    def setStatus(self, newStatus):
        self.__have = newStatus
    def setComment(self, newComment):
        self.__comment = newComment  