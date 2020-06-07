def validate_pin(pin):
    print (len(pin) in (4, 6) and pin.isdigit())

#main
validate_pin("123")
validate_pin("1234")
validate_pin("12a12")
validate_pin("123456")
