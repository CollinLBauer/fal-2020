def test(label, case, expected=NotImplemented):
    try:
        result = case()
        if result == expected or expected is NotImplemented:
            print(f'    PASS: {label}')
        else:
            print(f'(!) FAIL: {label} (found {repr(result)})')
    except Exception as ex:
        result = None
        print(f'(!) FAIL: {label} ({ex})')
    return result