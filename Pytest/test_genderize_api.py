#MAD - Pytest Assessment, Early Onboarding.
#Shakeel Akthar, SDET Intern @ MAD Street Den

import requests
import pytest

BASE_URL = "https://api.genderize.io"

@pytest.mark.parametrize("name, expected_gender", [("Akthar", "male"), ("Aishwaria", "female"),("Catherine", "female")])
def test_positive_proper_gender(name, expected_gender):
    response = requests.get(f"{BASE_URL}?name={name}")
    data = response.json()
    assert response.status_code == 200
    assert data["gender"] == expected_gender

def test_positive_details():
    name = "Shakeel"
    response = requests.get(f"{BASE_URL}?name={name}")
    data = response.json()
    assert response.status_code == 200
    assert "name" in data
    assert "gender" in data
    assert "probability" in data
    assert "count" in data

def test_negative_without_name():
    response = requests.get(BASE_URL)
    data = response.json()
    assert response.status_code == 422
    assert "error" in data
    assert data["error"] == "Missing 'name' parameter"

def test_multiple_names():
    names = ["Sanjay", "Varshini", "Akthar"]
    response = requests.get(f"{BASE_URL}", params={"name[]": names})
    data = response.json()
    assert response.status_code == 200
    for name in names:
        for item in data:
            if item["name"] == name:
                assert "gender" in item


#To Run: py.test

#RESULTS From Terminal!!

# PS E:\MAD\Early_onboarding\Pytest> py.test
# ================ test session starts ================

# platform win32 -- Python 3.10.11, pytest-7.4.2, pluggy-1.3.0
# rootdir: E:\MAD\Early_onboarding\Pytest
# plugins: anyio-3.6.2
# collected 6 items

# test_genderize_api.py ......                   [100%]

# ================= 6 passed in 6.75s =================
