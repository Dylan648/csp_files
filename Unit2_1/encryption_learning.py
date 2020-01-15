from passlib.hash import pbkdf2_sha256

hash = pbkdf2_sha256.hash('supersecret')
print(hash)

print(pbkdf2_sha256.verify('supersecret', hash))
print(pbkdf2_sha256.verify('wrong', hash))