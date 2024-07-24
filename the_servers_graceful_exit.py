# Simulate a server's main loop with a placeholder comment.
# Use a 'try-except-finaly' block to handle any potential exceptions during the server's runtime.
# In the 'finally' block, perform cleanup operations and print a shutdown mesage. 

try:
    print("Server is running...")
    raise Exception("Unexpected error!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Performing cleanup operation...")
    print("Shutting down server gracefully")