class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_text = []
        for string in strs:
            encoded_text.append(f"{len(string)}#{string}")
        return "".join(encoded_text)

    def decode(self, s: str) -> List[str]:
        decoded_text = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j+1
            j = i + length
            decoded_text.append(s[i:j])
            i = j

        return decoded_text