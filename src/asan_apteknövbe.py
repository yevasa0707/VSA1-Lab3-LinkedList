class Customer:
    def __init__(self, name, medicine):
        self.name = name
        self.medicine = medicine

class PharmacyQueue:

    def __init__(self):
        self.customers = []

    def addCustomer(self, name, medicine):
        customer = Customer(name, medicine)
        self.customers.append(customer)
        return customer

    def serveCustomer(self):
        if len(self.customers) == 0:
            print("Növbədə müştəri yoxdur.")
            return None

        customer = self.customers.pop(0)
        print(f"Xidmət göstərildi: {customer.name} - "
              f"{customer.medicine}")
        return customer

    def displayQueue(self):
        if len(self.customers) == 0:
            print("Növbə boşdur.")
            return

        for customer in self.customers:
            print(f"{customer.name} - {customer.medicine}")

    def countCustomers(self):
        return len(self.customers)


def main():
    pharmacy = PharmacyQueue()
    choice = ""

    while choice != "5":
        print("\n1. Müştəri əlavə et")
        print("2. İlk müştəriyə xidmət göstər")
        print("3. Növbəni göstər")
        print("4. Müştərilərin sayını göstər")
        print("5. Çıxış")

        choice = input("Seçim: ").strip()

        if choice == "1":
            name = input("Müştərinin adı: ")
            medicine = input("Dərmanın adı: ")

            if any(c.name == name for c in pharmacy.customers):
                print("Müştəri artıq növbədədir.")
                continue

            pharmacy.addCustomer(name, medicine)
            print("Müştəri növbəyə əlavə olundu.")

        elif choice == "2":
            pharmacy.serveCustomer()

        elif choice == "3":
            print("Aptekdəki növbə:")
            pharmacy.displayQueue()

        elif choice == "4":
            print("Müştərilərin sayı:",
                  pharmacy.countCustomers())

        elif choice != "5":
            print("Yanlış seçim.")

    print("Proqram bitdi.")


if __name__ == "__main__":
    main()
