def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Дефицит массы тела"
    elif 18.5 <= bmi < 25.0:
        return "Норма"
    elif 25.0 <= bmi < 30.0:
        return "Избыточная масса тела (предожирение)"
    else:
        return "Ожирение"

if __name__ == "__main__":
    w = float(input("Введите вес (кг): "))
    h = float(input("Введите рост (м): "))
    bmi_result = calculate_bmi(w, h)
    print(f"Ваш ИМТ: {bmi_result:.2f}")
    print(f"Интерпретация: {interpret_bmi(bmi_result)}")
# Проверено и готово к сдаче