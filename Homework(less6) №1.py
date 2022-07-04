from time import sleep


class TrafficLight:

    def running(self):

        count = 0
        while count < 3:
            self.__color = ["Красный", 'Желтый', "Зеленый"]
            print(self.__color[0])
            sleep(7)
            print(self.__color[1])
            sleep(2)
            print(self.__color[2])
            sleep(7)
            count += 1

traffic_light = TrafficLight()
traffic_light.running()

