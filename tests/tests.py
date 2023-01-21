import pytest

from nav.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestElements:

    def test_homepage_nav(self):
        homepage_nav = HomepageNav(self.driver)
        text = homepage_nav.get_nav_links()
        print(text)
