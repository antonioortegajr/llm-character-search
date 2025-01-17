import hashlib
import time
import requests
from datetime import datetime, timedelta

class MarvelAPI:
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        self.base_url = "https://gateway.marvel.com/v1/public"

    def _generate_auth_params(self):
        timestamp = str(int(time.time()))
        hash_input = timestamp + self.private_key + self.public_key
        hash_value = hashlib.md5(hash_input.encode('utf-8')).hexdigest()
        
        return {
            'ts': timestamp,
            'apikey': self.public_key,
            'hash': hash_value
        }

    def get_this_weeks_comics(self):
        """
        Fetches comics released this week from Marvel API
        Returns a list of comics with their details
        """
        # Calculate date range for this week
        today = datetime.now()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        # Format dates for API
        date_range = f"{start_of_week.strftime('%Y-%m-%d')},{end_of_week.strftime('%Y-%m-%d')}"

        # Build request parameters
        params = self._generate_auth_params()
        params.update({
            'dateRange': date_range,
            'orderBy': 'focDate',
            'limit': 100  # Adjust as needed
        })

        # Make API request
        response = requests.get(
            f"{self.base_url}/comics",
            params=params
        )

        if response.status_code == 200:
            data = response.json()
            return data['data']['results']
        else:
            raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
