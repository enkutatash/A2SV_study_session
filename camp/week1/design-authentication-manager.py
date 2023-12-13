class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ID=dict()
        self.timeToLive=timeToLive
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.ID[tokenId]=currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
            if tokenId in self.ID and self.ID[tokenId]+self.timeToLive>currentTime:
                self.ID[tokenId]=currentTime
            

    def countUnexpiredTokens(self, currentTime: int) -> int:
        unexpired=0
        for i,v in self.ID.items():
            if v+self.timeToLive>currentTime:
                unexpired+=1
        return unexpired

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)