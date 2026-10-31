from scanner import contains_secret

assert contains_secret('ctf{test_secret}')
assert not contains_secret('hello world')
print("All tests passed")
