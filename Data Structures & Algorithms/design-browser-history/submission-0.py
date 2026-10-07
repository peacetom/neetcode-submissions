class BrowserHistory:

    def __init__(self, homepage: str):
        home = Page(homepage)
        self.curr = home


    def visit(self, url: str) -> None:
        new_page = Page(url)
        self.curr.next = new_page
        new_page.prev = self.curr
        self.curr = new_page


    def back(self, steps: int) -> str:
        while steps > 0:
            if self.curr.prev == None:
                return self.curr.url
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.url
        

    def forward(self, steps: int) -> str:
        while steps > 0:
            if self.curr.next == None:
                return self.curr.url
            steps -= 1
            self.curr = self.curr.next
        return self.curr.url


class Page:

    def __init__(self, url: str):
        self.url = url
        self.prev = None
        self.next = None
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)