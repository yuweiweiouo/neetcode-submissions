import pickle
import base64
class Solution:

    def encode(self, strs: List[str]) -> str:
        dumped = pickle.dumps(strs)
        return base64.b64encode(dumped).decode('utf-8')

    def decode(self, s: str) -> List[str]:
        dumped = base64.b64decode(s.encode('utf-8'))
        return pickle.loads(dumped)
