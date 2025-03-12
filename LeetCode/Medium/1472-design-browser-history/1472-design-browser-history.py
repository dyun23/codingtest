class Node:
    def __init__(self, value = "", before = None, next = None):
        self.value = value
        self.before = before
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = self.current = Node(value=homepage)

    def visit(self, url: str) -> None:
        new_node = Node(value=url, before=self.current)
        self.current.next = new_node
        self.current = new_node

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.before != None:
            self.current = self.current.before
            steps -= 1
        return self.current.value

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next != None:
            self.current = self.current.next
            steps -= 1
        return self.current.value


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)