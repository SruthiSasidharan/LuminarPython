class swift:
    def start(self):
        print("swift start")
    def accelerate(self):
        print("swift accelerate")
    def stop(self):
        print("swift stop")

class seltos:
    def start(self):
        print("seltos start")

    def accelerate(self):
        print("seltos accelerate")

    def stop(self):
        print("seltos stop")

class person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.stop()
sw=seltos()
p=person()
p.drive(sw)