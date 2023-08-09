import pyshorteners

# Initialize a Shortener object
s = pyshorteners.Shortener()

# Long URL to be shortened
long_url = "https://www.example.com/this-is-a-very-long-url-that-needs-to-be-shortened"

# Shorten the URL
short_url = s.tinyurl.short(long_url)

print("Original URL:", long_url)
print("Shortened URL:", short_url)
