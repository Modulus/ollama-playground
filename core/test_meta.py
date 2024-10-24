from meta import extract_collection_name

def test_extract_collection_name() :   
    file = "files/nasjonal-digitaliseringsstrategi_ny.pdf" #, "files/nasjonal-digitaliseringsstrategi_ny.pdf"]
   

    assert "nasjonal_digitaliseringsstrategi_ny" == extract_collection_name(file)
