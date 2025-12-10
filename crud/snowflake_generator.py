import time
import random
import threading


class StringSnowflakeGenerator:

    def __init__(self):
        self.lock = threading.Lock()

    def _get_timestamp_ms(self) -> int:
        return int(time.time() * 1000)

    def generate_id(self) -> str:
        with self.lock:
            timestamp = str(self._get_timestamp_ms())
            random_part = str(random.randint(10000, 99999))
            final_id = f"{timestamp}{random_part}"
            return final_id
