class clsa():
    c = 100     # class attr
    __p1:int=0
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
        pass
    def getc(self):
        return self.__class__.c
    
    @staticmethod
    def staticM1(): # static Method, 不需要self
        return f"I'm staticM1: {__class__.c}."
    
    @classmethod
    def staticM2(cls): # static Method, 不需要self
        return f"I'm staticM2: {cls.c}."
    
    # 教學中說 不要用傳統的getter,setter, 這樣沒有pythonic, 可以使用以下方式
    @property       # 私有變數透過@property取得
    def p1(self):
        return self.__p1
    @p1.setter      # 私有變數透過.setter設定
    def p1(self, value):
        self.__p1 = value

a = clsa(2,3)
print(clsa.c, a.c, a.getc())
print(clsa.staticM1(), a.staticM1(), a.__class__.staticM1(), a.staticM2())
a.p1 = 999
print(f"p1: {a.p1}")

exit()
