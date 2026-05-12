import pytest  
from src.manager import Manager
from src.models import Parameters


def test_sprawdzenie_rozliczenia_lokatorów():
    parametry = Parameters(
        apartments_json_path="data/apartments.json",
        tenants_json_path="data/tenants.json",
        transfers_json_path="data/transfers.json",
        bills_json_path="data/bills.json"
    )
    manager = Manager(parametry)
    klucz_mieszkania = "apart-polanka"
    rok = 2025
    miesiac = 1

    roz = manager.get_settlement(
        apartment_key=klucz_mieszkania,
        year=rok,
        month=miesiac
    )
    
    roz_lok = manager.create_tenants_settlements(
        roz
    )
    suma_kosztow_mieszkania = roz.total_due_pln

    suma_naleznosci_lokatorow = sum(
        lokator.total_due_pln
        for lokator in roz_lok
    )

    assert suma_kosztow_mieszkania == suma_naleznosci_lokatorow, "Suma należności lokatorów nie zgadza się z sumą kosztów mieszkania"
