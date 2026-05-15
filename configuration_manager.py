import os
from dotenv import load_dotenv

class ConfigurationManager:
    def __init__(self):
        """
        Manages secure loading of environment variables and system constants.
        """
        # Load variables from a .env file if it exists
        load_dotenv()
        
        self.configs = {
            "GEMINI_API_KEY": os.getenv("GEMINI_API_KEY"),
            "DEFAULT_CURRENCY": os.getenv("DEFAULT_CURRENCY", "USD"),
            "MAX_RETRIES": 3,
            "TIMEOUT": 10
        }

    def get_config(self, key: str):
        """Provides access to API keys and other sensitive configurations."""
        value = self.configs.get(key)
        if value is None:
            print(f"Warning: Configuration for {key} is missing!")
        return value

    def validate_credentials(self) -> bool:
        """Ensure secure handling of credentials by checking if API keys are set."""
        gemini_key = self.get_config("GEMINI_API_KEY")
        if not gemini_key or gemini_key == "YOUR_API_KEY_HERE":
            return False
        return True