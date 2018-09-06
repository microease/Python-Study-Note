print("Let's practice everything.")
<<<<<<< HEAD
print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")
=======
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')
>>>>>>> 65f2110be20722ca7886b61a222c4d38b7fc5ef7
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
<<<<<<< HEAD
print("---------------------")
print(poem)
print("---------------------")
five = 10 - 2 + 3 - 6
print("This should be five:%s" % five)


def secret_formata(started):
    jelly_beans = started * 5
=======
print("--------------")
print(poem)
print("--------------")
five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)


def secret_formula(started):
    jelly_beans = started * 500
>>>>>>> 65f2110be20722ca7886b61a222c4d38b7fc5ef7
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
<<<<<<< HEAD
beans, jars, crates = secret_formata(start_point)


=======
beans, jars, crates = secret_formula(start_point)
print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))
start_point = start_point / 10
print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))
>>>>>>> 65f2110be20722ca7886b61a222c4d38b7fc5ef7
