def test_display_message():
    try:
        display_message()
        return True
    except:
        return False

def main():
    test_suite = [test_display_message]
    for test in test_suite:
        if test():
            print(f"{test.__name__}: PASSED")
        else:
            print(f"{test.__name__}: FAILED")

if __name__ == "__main__":
    main()