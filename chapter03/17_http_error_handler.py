def get_http_error(error_code):
    error_messages = {200: "OK", 400: "Bad request", 404: "Not found"}
    return error_messages.get(error_code, "Unknown Error") 

# .get() returns the value for the given key if it exists,
# otherwise returns the default ("Unknown Error").
# Functionally similar to a match/case with a default (_) branch.

def main():
    error_code = 404
    print(get_http_error(error_code))

if __name__ == "__main__":
    main()