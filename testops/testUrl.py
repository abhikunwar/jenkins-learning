from util.read_ini import read_ini
from util.apiutils import getPetdata,postPetdata
import pytest
petId = '198'

@pytest.fixture
def add_pet():
    config_obj = read_ini()
    BaseUrl = config_obj['pet']['url']
    payload = {'id':int(petId),'name':'Cuitee','status':'Available'}
    resp = postPetdata(BaseUrl,payload)
    pet_id = resp.json()['id']
    yield pet_id

def test_GetReq(add_pet):
    headers = {'Content-Type':'application/json'}
    config_obj = read_ini()
    BaseUrl = config_obj['pet']['url']
    url = BaseUrl + str(add_pet)
    response = getPetdata(url,headers=headers)
    assert response.json()
    
    assert response.status_code == 200
    print(response.json())

testdata = [
    ('available',200),
    ('pending',200),
    ('sold',200)
]
@pytest.mark.parametrize("type , status",testdata)
def test_status(type,status):
    config_obj = read_ini()
    BaseUrl = config_obj['pet']['url']
    url = BaseUrl + 'findByStatus'
    param = {'status': type}
    response = getPetdata(url,params=param)
    assert response.status_code == status 
    print(response)



