#FirstClassFunction
def div(dividend,divisor) -> float:
    if divisor == 0:
        raise ZeroDivisionError("Division not possible")
    return dividend/divisor

def calculate(*values,operator): 
    return operator(*values) # calling operator var as func
try:
    result = calculate(20,4, operator=div)
except ZeroDivisionError as e:
    print(e)

print(result)

def search(sequence,expected, finder):
    for element in sequence:
        if finder(element) == expected:
            return element
    raise RuntimeError(f"Cant find the search term")

friends = [{"name":"Rob"},{"name":"Bob"},{"name":"Jon"}]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Rob",get_friend_name))


print(search(friends, "Rob",lambda friend:friend["name"]))
