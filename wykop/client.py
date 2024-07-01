from typing import Optional

class BaseWykopClient:

    API_URL = "https://wykop.pl/api/v3/"

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
    ):
        self.API_KEY = api_key
        self.API_SECRET = api_secret

