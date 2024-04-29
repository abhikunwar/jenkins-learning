from util.read_ini import read_ini
def test_method1():
    assert 5 + 3 == 8

def test_pet_url():
    config = read_ini()
    url_name = config['pet']['url']
    print(url_name)
    assert 'petstore' in url_name   
