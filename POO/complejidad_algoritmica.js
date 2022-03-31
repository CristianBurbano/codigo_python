function factorial(n) {
  let respuesta = 1;
  while (n > 1) {
    respuesta = math.multiply(respuesta, n);
    n--;
  }
  return respuesta;
}
function factorial_r(n) {
  if (n == 1) respuesta = 1;
  else return n * factorial_r(n - 1);
}

math.config({ precision: 2000 });

n = 2000;
console.log(`n= ${n}`);
comienzo = new Date();
r = factorial(n);
final = new Date();
console.log(`r=${r} t(ms)=${final - comienzo}`);

// comienzo = new Date();
// factorial_r(n);
// final = new Date();
// console.log(final - comienzo);
