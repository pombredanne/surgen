from surgen import Procedure

class DoNothing(Procedure):

    def operate(self):
        print(self.root)
