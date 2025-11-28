import time

# Get the timestamp (seconds since January 1, 1970)
timestamp = time.time()

# Format with commas and 4 decimals
formatted_timestamp = f"{timestamp:,.4f}"

# Scientific notation with 2 decimals
scientific_notation = f"{timestamp:.2e}"

# Get current date
current_time = time.localtime()
date_formatted = time.strftime("%b %d %Y", current_time)

# Display results
print(f"Seconds since January 1, 1970: {formatted_timestamp} or "
      f"{scientific_notation} in scientific notation")
print(date_formatted)
