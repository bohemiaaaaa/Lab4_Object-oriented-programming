def total_price(price: float, tax: float) -> float:
    return price + price * tax


def repeater(s: str, n: int) -> str:
    return s * n


def greet(name: str = "Гость") -> str:
    return f"Здравствуйте, {name}!"


def log_message(msg: str) -> None:
    print(f"[LOG] {msg}")
