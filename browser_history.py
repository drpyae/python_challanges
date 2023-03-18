class BrowserHistory:
  """
    In the __init__ method, we initialize the history list with the homepage and set current to 0 (indicating the current page).
  The visit method takes a url parameter and adds it to the history list after clearing all the forward history. 
  The current index is updated accordingly.
  The back method takes a steps parameter and moves back in history by steps number of steps. 
  If steps is greater than the number of steps we can move back, we set current to 0. We then return the current page after moving back in history.
  The forward method takes a steps parameter and moves forward in history by steps number of steps.
  If steps is greater than the number of steps we can move forward, we set current to the last index of history.
  We then return the current page after moving forward in history.
  """

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0
        

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current+1]
        self.history.append(url)
        self.current += 1
        

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]
        

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
