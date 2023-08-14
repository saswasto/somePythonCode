def voter(age):
    if age <18:
        raise ValueError("invalid voter")
    return "You are allowed to vote "
try:
    print(voter(18))
    print(voter(17))
except ValueError as e:
    print(e)