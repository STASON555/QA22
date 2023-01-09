import pytest

from homepage_nav.Homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomePage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        print(homepage_nav.get_nav_links_text())