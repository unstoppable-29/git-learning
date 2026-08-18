# Calculate the result
result = 2 + 2
expected = 4

# Check if the result is correct
if result == expected:
    print("Success: 2 + 2 equals 4! The test passed.")
else:
    # The 'raise Exception' command crashes the script intentionally
    raise Exception("Test Failed! Math is broken.")