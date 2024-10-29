from prompt import list_collections

def test_list_collections_is_not_empty():
    collections = list_collections()

    assert collections is not None
    assert len(collections) >= 1

def test_list_collections_has_all_needed_collections():
    collections = list_collections()

    assert "IPSC_Pistol_Caliber_Carbine_Competition_Rules_Jan_2024_Edition_Final_27_Dec_2023" in collections
    assert "nasjonal_digitaliseringsstrategi_ny" in collections
    assert "stm202320240031000dddpdfs" in collections