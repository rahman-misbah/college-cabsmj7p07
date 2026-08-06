# User Preference dictionary
user_preference = {
    "theme": "dark",
    "notifications": True,
    "language": "en-US",
    "font_size": 14
}

# Get value of currency
currency = user_preference.get("currency", "USD")

# Update font size to 16
user_preference["font_size"] = 16

# Remove "notifications" safely
user_preference.pop("notifications", "Preference not found!")

for key in user_preference:
    print(f"{key}:{user_preference[key]}")