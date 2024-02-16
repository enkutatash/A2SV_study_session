class site:
    def __init__(self,url):
        self.url=url
        self.forward=None
        self.back=None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head=site(homepage)

    def visit(self, url: str) -> None:
        page=site(url)
        page.back=self.head
        self.head.forward=page
        self.head=self.head.forward
        

    def back(self, steps: int) -> str:
        while steps and self.head.back:
            self.head=self.head.back
            steps-=1
        return self.head.url

        

    def forward(self, steps: int) -> str:
        while steps and self.head.forward:
            self.head=self.head.forward
            steps-=1
        return self.head.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)