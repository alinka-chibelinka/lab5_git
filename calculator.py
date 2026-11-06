def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

if __name__ == "__main__":
    w = float(input("Введите вес (кг): "))
    h = float(input("Введите рост (м): "))
    print(f"Ваш ИМТ: {calculate_bmi(w, h):.2f}")