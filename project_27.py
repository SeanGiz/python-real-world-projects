from dataclasses import dataclass

@dataclass
class Product:
    name: str
    quantity: int
    unit_price: float

    def stock_value(self):
        return self.quantity * self.unit_price


def main():
    item = Product("Notebook", 3, 4.5)
    print(f"{item.name}: {item.stock_value():.2f}")


if __name__ == "__main__":
    main()
