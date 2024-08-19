from typing import Optional
class Chain:
    def __init__(self, nextChan: Optional['Chain'] = None):
        self.nextChan = nextChan

    def next(self, request):
        if(self.nextChan == None):
            return True
        self.nextChan.handle(request)
        
class C1(Chain):
    def handle(self, request):
        print("c1 pass")
        # if(request != "sharaf"):
        #     print("Request cannot be handled by C1")
        #     return False
        return self.next(request)

class C2(Chain):
    def handle(self, request):
        print("c2 pass")
        # if(request != "sharaf"):
        #     print("Request cannot be handled by C1")
        #     return False
        return self.next(request)

class C3(Chain):
    def handle(self, request):
        print("c3 pass")
        # if(request != "sharaf"):
        #     print("Request cannot be handled by C1")
        #     return False
        return self.next(request)

chainCombination = [
    C1,
    C2,
    C3  # Add more chain classes as needed here.
]
def handleRequest(request):
    for index, chain in  enumerate(chainCombination):
        if index + 1 <= len(chainCombination):
            print(index)
            chainCombination[index] = chain(chainCombination[index+1]())
    
    return chainCombination[0].handle(request)




def main():
    # inp = input('What is your name: ')
    # if(not handleRequest(inp)):
    #     return
    handleRequest('inp')
    print("Welcom")

main()