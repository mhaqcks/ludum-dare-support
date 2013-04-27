
# t: current time, b: begInnIng value, c: change In value, d: duration

def linearTween(t, b, c, d):
	return c * t / d + b

def easeInQuad(t, b, c, d):
	t /= d
	return c * t ** 2 + b

def easeOutQuad(t, b, c, d):
	t /= d
	return -c * t * (t - 2) + b

def easeInOutQuad(t, b, c, d):
	t /= d / 2

	if t < 1:
		return c / 2  * t ** 2 + b
	t -= 1
	return -c / 2 * (t * (t - 2) - 1) + b
