print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print("---------------------")
print(poem)
print("---------------------")
five = 10 - 2 + 3 - 6
print("This should be five:%s" % five)


def secret_formata(started):
    jelly_beans = started * 5
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formata(start_point)


