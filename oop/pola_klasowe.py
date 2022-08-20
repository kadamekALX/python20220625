class JakasKlasa:
    # pola klasowe są przechowywane wewnątrz _klasy_, a nie wewnątrz jej obiektów
    POLE_KLASOWE = 100

    def __init__(self):
        print("Tworze obiekt")
        JakasKlasa.POLE_KLASOWE = 200 # dostęp do pola klasowego wymaga zawsze poprzedzenia nazwy pola nazwą klasy


print(JakasKlasa.POLE_KLASOWE) # dostęp do pola klasowego nie wymaga stowrzenia żadnego obiektu
JakasKlasa.POLE_KLASOWE = 150
print(JakasKlasa.POLE_KLASOWE)
x = JakasKlasa()
print(JakasKlasa.POLE_KLASOWE)

