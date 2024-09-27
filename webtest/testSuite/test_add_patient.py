from webtest.conftest import setup
from webtest.page.login_page import LoginPage
from webtest.page.patient_page import PatientPage


def test_add_patient(setup):
    setup.get("http://demo.openemr.io/b/openemr/")

    login_page = LoginPage(setup)
    login_page.enter_username("admin")
    login_page.enter_password("pass")
    login_page.select_language()
    login_page.click_login()

    patient_page = PatientPage(setup)
    patient_page.click_patient()
    patient_page.click_new_search()
    patient_page.add_patient_details("uma", "sankar")
    patient_page.select_dob()
    patient_page.select_gender()
    patient_page.create_new_patient()


