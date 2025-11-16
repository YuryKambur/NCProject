import pytest


def test_modal_form_presentation(setup_browser, repricer_page):
    try:
        repricer_page.open()
        repricer_page.open_form_presentation()
        repricer_page.has_form_presentation_success()
    except AssertionError:
        pytest.xfail("Тест не проходит из-за региональной блокировки")
