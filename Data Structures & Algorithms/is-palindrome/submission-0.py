class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric characters and convert to lowercase
        cleaned_str = "".join(char.lower() for char in s if char.isalnum())
        
        # Check if the cleaned string reads the same backwards
        return cleaned_str == cleaned_str[::-1]

 
        