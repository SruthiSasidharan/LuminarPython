class pycharm:
    def create_file(self):
        print("pycharm file created")
    def execute_file(self):
        print("pycharm file executed")


class vscode:
    def create_file(self):
        print("vscode file created")

    def execute_file(self):
        print("vscode file executed")

class programmer:
    def coding(self,ide):
        ide.create_file()
        ide.execute_file()
py=vscode()
p=programmer()
p.coding(py)