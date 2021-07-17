import requests
import pprint
import os

url = "http://localhost:5000/"
template_name = "t1"


def test_list_templates():
    r = requests.get(url=url + "/api/v1/templates")
    print(r, r.ok)
    print(r.json())
    assert r.ok


def test_upload_template():
    file = {'file': open(os.path.abspath("app-files/current/" + template_name + ".yaml"), 'rb')}
    headers = {}
    data = {}
    # data = {"tmpl_id": "2"}

    r = requests.post(url=url + "/api/v1/templates", headers=headers, data=data, files=file)
    print(r, r.ok)
    print(r.json())
    assert r.ok


def test_install_template():
    tmpl_id = template_name
    r = requests.post(url=url + "/api/v1/templates/" + tmpl_id + "/install")
    print(r, r.ok)
    pprint.pprint(r.json())
    assert r.ok


def test_delete_template():
    r = requests.get(url=url + "/api/v1/templates")
    number_of_templates = len(r.json()['templates'])

    tmpl_id = template_name
    r = requests.delete(url=url + "/api/v1/templates/" + tmpl_id)
    print(r, r.ok)
    print(r.json())
    assert r.ok

    r = requests.get(url=url + "/api/v1/templates")
    number_of_templates2 = len(r.json()['templates'])
    assert number_of_templates - 1 == number_of_templates2  # Assert the number of templates is correct
