def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager()
print(avg(10))
print(avg(1))
print(avg(12))

print(f"Local variables of a function: {avg.__code__.co_varnames}")
print(f"Closure variables of a function: {avg.__code__.co_freevars}")
print(
    f"Count value of a function: {avg.__closure__[0].cell_contents}, \
    total value of a function: {avg.__closure__[1].cell_contents}"
)
