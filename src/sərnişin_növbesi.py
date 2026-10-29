class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class BusQueue:
    def __init__(self):
        self.priority = []
        self.normal = []

    def addPassenger(self, name, age):
        p = Passenger(name, age)

        if age > 65:
            self.priority.append(p)
            print("Prioritet növbəsinə əlavə olundu.")
        else:
            self.normal.append(p)
            print("Adi növbəyə əlavə olundu.")

    def boardPassenger(self):
        if len(self.priority) > 0:
            p = self.priority.pop(0)
            print("Avtobusa mindi:", p.name)

        elif len(self.normal) > 0:
            p = self.normal.pop(0)
            print("Avtobusa mindi:", p.name)

        else:
            print("Növbə boşdur.")

    def displayQueue(self):
        print("Prioritet növbəsi:")
        if len(self.priority) == 0:
            print("Boşdur.")
        else:
            for p in self.priority:
                print(p.name, "-", p.age)

        print("Adi növbə:")
        if len(self.normal) == 0:
            print("Boşdur.")
        else:
            for p in self.normal:
                print(p.name, "-", p.age)

    def countPassengers(self):
        return len(self.priority) + len(self.normal)


def main():
    bus = BusQueue()
    choice = ""

    while choice != "5":
        print("\n1. Sərnişin əlavə et")
        print("2. Avtobusa sərnişin mindir")
        print("3. Növbələri göstər")
        print("4. Sərnişinlərin sayını göstər")
        print("5. Çıxış")

        choice = input("Seçim: ")

        if choice == "1":
            name = input("Sərnişinin adı: ")
            age = int(input("Sərnişinin yaşı: "))
            bus.addPassenger(name, age)

        elif choice == "2":
            bus.boardPassenger()

        elif choice == "3":
            bus.displayQueue()

        elif choice == "4":
            print("Növbədəki sərnişinlərin sayı:",
                  bus.countPassengers())

        elif choice == "5":
            print("Proqram bitdi.")

        else:
            print("Yanlış seçim!")


if __name__ == "__main__":
    main()
