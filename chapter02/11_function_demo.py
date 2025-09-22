def say_hello(name: str = "User"):        #def = definition
    """
    Print a greeting message.
    
    Args:
        name (str): The name to greet. Default value 'User'
    """
    print(f"Hello {name}")

def main():
  #say_hello("Panos")
  #say_hello(10)
  say_hello()
  say_hello("Panos")
  #print(say_hello.__doc__)
  print(help(say_hello))
  pass

if __name__ == "__main__":
  main()