# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

'''My Solution'''
def validate_pin(PIN):
    return True if PIN.isdigit() and str(len(PIN)) in '46' else False

'''Best Solution'''
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
