# Password Generator

This code generates a random password using either the `random` or `secrets` module. The password will be of length 12 by default, but this can be changed by providing a different value for `pwd_length` when calling the `generate_password()` function.

The password is generated by choosing random characters from a combination of uppercase letters, lowercase letters, digits, and punctuation. The password is then checked to ensure it contains at least one of each of these character types, and if not, a new password is generated.

To generate a password using the `random` module, call the `generate_password()` function with no arguments or with a custom value for `pwd_length`:

```python
password = generate_password()
print(password)

password = generate_password(16)
print(password)
```
To generate a password using the secrets module, call the generate_password() function with the use_secrets=True argument:

```python
password = generate_password(use_secrets=True)
print(password)

password = generate_password(16, use_secrets=True)
print(password)
```