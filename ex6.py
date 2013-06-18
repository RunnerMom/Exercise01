#assign variable x to string. substitute value 10 for %d
x ="tHERE ARE %d TYPES OF PEOPLE" %	10
#assigns string to variable binary
binary = "binary" 
#assigns string to variable do_not
do_not = "don't"
# assigns variable Y to string. Substitutes variables binary and do_not
y = "Those who know %s and those who %s" % (binary, do_not)
#prints string held by variable x
print x
#prints string held by variable y
print y
#substitutes string held by variable x into print string
print "I said: %r." % x
#substitutes string help by variable y into print string
print "I also said: '%s'." % y
#assigns variable hilarious to boolean F
hilarious = False
#assigns variable to a string with a substitution call
joke_evalutaion = "Isn't that joke so funny?! %r"
#prints contents of two variables
print joke_evalutaion % hilarious
#assigns new strings
w = "This is the left side of ..."
e = "a string with a right side."
#prints concatenation of strings held by two variables
print w + e