def myfun():
    print("Hello Module")
myfun()

# we can import this up
# but the down part we can't import cuz it use---
if __name__ == "__main__":
    myfun()
    #if this code is directly executed by running the file its present in
    print("We are directly running this code")
    print(__name__)

    #if __name__ == "__main__":
# is a Python way of saying “run this part only if the script is executed directly, not when imported