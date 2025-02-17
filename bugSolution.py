def function_with_error_handling(a, b):
    try:
        if a == 0:
            return float('inf')  # Return infinity instead of error
        return a + b
    except Exception as e:
        return f"An error occurred: {e}"