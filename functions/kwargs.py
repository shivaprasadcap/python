def display_info(greeting, *args, **kwargs):
    print(greeting)
    for arg in args:
        print(f"Positional argument: {arg}")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

display_info("Hello", "Alice", "Bob", age=30, city="New York")
