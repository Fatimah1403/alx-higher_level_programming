#!/usr/bin/node

const x = parseInt(process.argv[2]);

function factorial (n) {
	if (x === 0 || isNaN(x)) {
		return 1;
	}

	return x * factorial(x - 1);
}
console.log(factorial(x));
