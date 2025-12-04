from sixth import download_url_and_get_all_hrefs
from unittest.mock import MagicMock
import requests


def test_download_url_and_get_all_hrefs():
    data = '<html><body><a id="1" href="https://www.jcu.cz">odkaz</a><div><a href="http://ef.jcu.cz/kontakty">kontakty</a></div></body></html>'

    requests.get = MagicMock(
        return_value = MagicMock(ok=True, content=data)
    )

    href = download_url_and_get_all_hrefs('xxx')

    assert href == ['https://www.jcu.cz', 'http://ef.jcu.cz/kontakty']