import pytest
import os
from playwright.sync_api import Page
from pages.page_manager import PageManager
import os
@pytest.fixture(scope="session")
def base_url():
    BASE_URL_UI = os.environ.get("BASE_URL_UI", "http://localhost:5173")
    return BASE_URL_UI
@pytest.fixture
def page_manager(page:Page, base_url:str) -> PageManager:
    page.goto(base_url)
    return PageManager(page)
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return ({
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
    })