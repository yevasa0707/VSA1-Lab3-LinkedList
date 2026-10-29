class Customer:
    def __init__(self, name, medicine):
        self.name = name
        self.medicine = medicine


class PharmacyQueue:
    def __init__(self):
        self.customers = []

    def addCustomer(self, name, medicine):
        self.customers.append(Customer(name, medicine))
        print("Müştəri əlavə olundu.")

    def serveCustomer(self):
        if len(self.customers) == 0:
            print("Növbə boşdur.")
        else:
            c = self.customers.pop(0)
            print("Xidmət göstərildi:", c.name, "-", c.medicine)

    def displayQueue(self):
        if len(self.customers) == 0:
            print("Növbə boşdur.")
        else:
            for c in self.customers:
                print(c.name, "-", c.medicine)

    def removeCustomer(self, name):
        for c in self.customers:
            if c.name.lower() == name.lower():
                self.customers.remove(c)
                print("Müştəri silindi.")
                return

        print("Müştəri tapılmadı.")

    def countCustomers(self):
        return len(self.customers)


def main():
    pharmacy = PharmacyQueue()
    choice = ""

    while choice != "6":
        print("\n1. Müştəri əlavə et")
        print("2. İlk müştəriyə xidmət göstər")
        print("3. Növbəni göstər")
        print("4. Müştərilərin sayını göstər")
        print("5. Müştərini sil")
        print("6. Çıxış")

        choice = input("Seçim: ")

        if choice == "1":
            name = input("Müştərinin adı: ")
            medicine = input("Dərmanın adı: ")
            pharmacy.addCustomer(name, medicine)

        elif choice == "2":
            pharmacy.serveCustomer()

        elif choice == "3":
            pharmacy.displayQueue()

        elif choice == "4":
            print("Müştərilərin sayı:", pharmacy.countCustomers())

        elif choice == "5":
            name = input("Silinəcək müştərinin adı: ")
            pharmacy.removeCustomer(name)

        elif choice == "6":
            print("Proqram bitdi.")

        else:
            print("Yanlış seçim!")


if __name__ == "__main__":
    main()
