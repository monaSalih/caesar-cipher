from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import (encrypt, decrypt ,crack)

def test_version():
    assert __version__ == '0.1.0'

def  test_encrypt_with_shift():
    actuall = encrypt ("Lab18 In Level401 pyThon",3)
    expected = "Ode18 Lq Ohyho401 sbWkrq"
    assert actuall == expected

def  test_decrypt_with_shift():
    actuall = decrypt ("Ode18 Lq Ohyho401 sbWkrq",3)
    expected = "Lab18 In Level401 pyThon" 
    assert actuall == expected

def  test_upper_case():
    actuall = encrypt ("THIS CODE SHOULD HANDLE UPPER CASE",3)
    expected = "WKLV FRGH VKRXOG KDQGOH XSSHU FDVH" 
    assert actuall == expected

def  test_lower_case():
    actuall = encrypt ("this code should handle lower case",3)
    expected = "wklv frgh vkrxog kdqgoh orzhu fdvh" 
    assert actuall == expected