
from embed import list_files

def test_embed_get_files():
    files = list_files("files")
    assert files is not None
    assert len(files) >= 3


def test_embed_get_files_with_postfix():
    files = list_files("files", postfix=".pdf")
    assert files is not None
    assert len(files) >= 3
    assert "files/nasjonal-digitaliseringsstrategi_ny.pdf" in files
    assert "files/IPSC-Pistol-Caliber-Carbine-Competition-Rules-Jan-2024-Edition-Final-27-Dec-2023.pdf" in files
    assert "files/stm202320240031000dddpdfs.pdf" in files
    assert "files/swift-iso20022fordummies-6thedition-2022.pdf" in files