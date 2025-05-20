def divide(a, b):
    return a /b

try:
    teste = divide(10, 0)
    print(f"{teste:.2f} foi!")
except Exception:
    print(f"Um erro ocorreu")
finally:
    print('Fim da execução!')