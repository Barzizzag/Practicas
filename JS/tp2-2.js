console.log("Parte de arrays")
/*
//AP ejercicio 19-20
let edades = [12, 12, 23, 45, 34, 56, 34, 45, 65, 34];
let long = edades.length;
let i = 0;
console.log(long);
while (i < long) {
    console.log(edades[i])
    i++
}

let par = 0;
for (i = 0; i < long; i++) {
    par = edades[i] % 2;
    par == 0 ? console.log(edades[i]) : par = 0; //Operador ternario (se puede evitar la segunda opcion??)
}
*/
/*
//AP ejercicio 21-22-23
let numeros = [3, 6, 67, 6, 23, 11, 100, 8, 93, 0, 17, 24, 7, 1, 33, 45, 28, 33, 23, 12, 99, 100];
let long = numeros.length
let i = 0
let min = numeros[i]
let max = numeros[i]
function minimo(numeros, long) {
    for (i = 0; i < long; i++) {
        if (min > numeros[i]) {
            min = numeros[i]
        };
    }
    return (min)
}
function maximo(numeros, long) {
    for (i = 0; i < long; i++) {
        if (max < numeros[i]) {
            max = numeros[i]
        };
    }
}
function conIndex(numeros, indice) {
    console.log("El numero en la posicion " + indice + " es " + numeros[indice])
}
minimo(numeros, long)
console.log("El numero mas chico es: " + min);
maximo(numeros, long)
console.log("El numero mayor es: " + max)
let indice = 0
let salida = false
while (salida == false) {
    indice = parseInt(prompt("Ingrese un numero entre 0 y " + long))
    if (indice <= long) {
        salida = true
    };
}
conIndex(numeros, indice)
*/
/*
//AP ejercicio 24
let array = [3, 6, 67, 6, 23, 11, 100, 8, 93, 0, 17, 24, 7, 1, 33, 45, 28, 33, 23, 12, 99, 100];
let array2 = [];
let num1 = 0;
let num2 = 0;
function repite(array, num1, num2) {
    let a = 0;
    let b = 0;
    for (a = 0; (a < array.length); a++) {
        num1 = array[a]
        for (b = (a + 1); (b < array.length); b++) {
            if (num1 == num2) {

                array2 = num1;
            }
        }
    }
}
*/
//Ejercicio 25

//Ejercicio 26

let n = prompt("Ingrese un numero")
let arr = n.split('');
let arr2 = [];
let longA1 = arr.length;
let longA2 = arr2.length;

//console.log ("array 1: "+longA1+" aray 2 "+longA2)
for (i = 0; i < longA1; i++) {
    let ind = longA1 - i - 1
    arr2[i] = arr[ind]
    console.log("array1 " + arr[i] + " array 2 " + arr2[i])
};

for (b = 0; b < longA2; b++) {
    console.log(arr2[b])
    console.log("no entra al for?")
};
