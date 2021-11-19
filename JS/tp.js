console.log("Aca comienzan el trabajo")

/*
//AP1 ejercicio 1

console.log ("Hola mundo")
*/
/*
//AP1 ejercicio 2

document.writeln ("Hola mundo!!! ")
*/
/*
//AP1 ejercicio 3

document.writeln ("La suma de 3 + 5 es :" + parseInt(3+5))
*/
/*
//*AP1 ejercicio 4

let nombre = prompt ("Ingrese su nombre")
document.writeln ("Hola " +nombre)
*/
/*
//AP1 ejercicio 5

let x = parseInt( prompt ("Escriba el primer numero "))
let y = parseInt( prompt ("Escriba otro numero "))
document.writeln ("La suma de los numeros es " + parseInt(x+y))
*/
/*
//AP1 ejercicio 6

let x6 = parseInt( prompt ("Escriba el primer numero "))
let y6 = parseInt( prompt ("Escriba otro numero "))
if (x6 > y6) {
    document.writeln (x6 + " es mayor")
} else if (x6 == y6){
    document.writeln("Ambos son iguales")
}else{
     document.writeln(y6 + " es mayor")
}
*/
/*
//AP1 ejercicio 7

let x7 = parseInt(prompt("Escriba el primer numero"))
let y7 = parseInt(prompt("Escriba el segundo numero"))
let z7 = parseInt(prompt("Escriba el ultimo numero"))
if (x7 > y7) {
    if (x7 > z7) {
        document.writeln("El primer numero es el mayor")
    } else {
        document.writeln("El tercer numero es el mayor")
    }
} else if (x7 < y7) {
    if (y7 > z7) {
        document.writeln("El segundo numero es el mayor")
    } else {
        document.writeln("El tercer numero es el mayor")
    }
} else {
    document.writeln("Son todos iguales")
}
*/
/*
//AP ejercicio 8

let x8 =parseInt(prompt("Ingrese un numero"))
let divis= x8%2
if (divis==0){
    document.writeln (x8 + " es divisible por 2")
} else {
    document.writeln (x8 + " no es divisible por 2")
}
*/
/*
//AP ejercicio 9

let frase = prompt("Escriba una frase)")
let contador = 0
let result = ""
frase = frase.toLowerCase()
for (let i = 0; i < frase.length; i++) {
    result = frase.charAt(i)
    if ((result == "a") | (result == "á")) {
        contador += 1
    }
}
document.writeln(contador)
*/
/*
//AP ejercicio 10

let frase = prompt("Escriba una frase)")
let result = ""

frase = frase.toLowerCase()
for (let i = 0; i < frase.length; i++) {
    result = frase.charAt(i)
    if ((result == "a") | (result == "á") |
    (result == "e") | (result == "é") |
    (result == "i") | (result == "í") |
    (result == "o") | (result == "ó") |
    (result == "u") | (result == "ú") | (result == "ü")) {
        document.writeln(result)
    }
}
*/
/*
//AP ejercicio 11

let frase = prompt("Escriba una frase)")
let result = ""
let contador = 0
frase = frase.toLowerCase()
for (let i = 0; i < frase.length; i++) {
    result = frase.charAt(i)
    if ((result == "a") | (result == "á") |
        (result == "e") | (result == "é") |
        (result == "i") | (result == "í") |
        (result == "o") | (result == "ó") |
        (result == "u") | (result == "ú") | (result == "ü")) {
        contador += 1
    }
}
document.writeln(contador)
*/
/*
//AP ejercicio 12

let frase = prompt("Escriba una frase)")
let result = ""
let contA = 0
let contE = 0
let contI = 0
let contO = 0
let contU = 0
frase = frase.toLowerCase()
for (let i = 0; i < frase.length; i++) {
    result = frase.charAt(i)
    if ((result == "a") | (result == "á")){
        contA+=1
    }else if((result == "e") | (result == "é")){
        contE+=1
    }else if((result == "i") | (result == "í")){
        contI+=1
    }else if((result == "o") | (result == "ó")){
        contO+=1
    }else if ((result == "u") | (result == "ú") | (result == "ü")){
        contU+=1
    }
}
document.writeln("En la frase hay "+contA+"letras a")
document.writeln("En la frase hay "+contE+"letras e")
document.writeln("En la frase hay "+contI+"letras i")
document.writeln("En la frase hay "+contO+"letras o")
document.writeln("En la frase hay "+contU+"letras u")
*/
/*
//AP ejercicio 13

let x13=parseInt(prompt("Escriba un numero"))
let div2=x13%2
let div3=x13%3
let div5=x13%5
let div7=x13%7
//Salida si no es divisible
if ((div2!=0)&(div3!=0)&(div5!=0)&(div7!=0)){
    document.writeln("no es divisible")
}
//Salida si es divisible
if ((div2==0)|(div3==0)|(div5==0)|(div7==0)){
    document.writeln("Es divisible")
}
*/
/*
for (let i = 0; i < 4; i++) {
    if (div2==0){
        document.writeln("es divisible por 2")
    }
    if(div3==0){
        document.writeln("es divisiblepor 3")
    }
    if(div5==0){
        document.writeln("es divisible por 5")
    }
    if(div7==0){
        document.writeln("es divisible por 7")
    }
    if ((div2!=0)&(div3!=0)&(div5!=0)&(div7!=0)){
        document.writeln("no es divisible")
    }
}
*/
/*
//AP ejercicio 14

let x14=parseInt(prompt("Escriba un numero"))
let div2=x14%2
let div3=x14%3
let div5=x14%5
let div7=x14%7

if (div2==0){
    document.writeln("es divisible por 2")
}
if(div3==0){
    document.writeln("es divisiblepor 3")
}
if(div5==0){
    document.writeln("es divisible por 5")
}
if(div7==0){
    document.writeln("es divisible por 7")
}
if ((div2!=0)&(div3!=0)&(div5!=0)&(div7!=0)){
    document.writeln("no es divisible")
}
*/
/*
//AP ejercicio 15

let x15=parseInt(prompt("Igrese un numero"))
for (let i = 1; i <= x15; i++){
    let div=x15%i
    if (div==0){
        document.writeln(x15+" divisible por "+i)
    }

}
*/
/*
//AP ejercicio 16

let x16 = parseInt(prompt("Ingrese el primer numero"))
let y16 = parseInt(prompt("Ingrese el segundo numero"))
let menor = 0
if (x16 > y16) {
    menor = x16
} else {
    menor = y16
}
for (let i = 1; i <= menor; i++) {
    let div1 = x16 % i
    let div2 = y16 % i
    if ((div1 == 0) & (div2 == 0)) {
        document.writeln(i + " es divisor de ambos numeros")
    }
}
*/
/*
//AP ejercicio 17

let x17=parseInt(prompt("Ingrese un numero"))
let primo=true
for (let i=2; i<=(x17-1);i++){
    let div=x17%i
    if (div==0){
        primo=false
    }
}
if (primo==true){
    document.write(x17+" es primo")
}else{
    document.write(x17+" no es primo")
}
*/
/*
//AP ejercicio 18

let x18=parseInt(prompt("Ingrese la edad"))
if (x18>18){
    document.writeln("Ya puedes manejar")
}
*/
/*
//AP ejercicio 19

let x19 = parseInt(prompt("Ingrese su calificacion"))
if (x19 < 3) {
    console.log("Muy deficiente")
} else if (x19 < 5) {
    console.log("Insuficiente")
} else if (x19 < 6) {
    console.log("Suficiente")
} else if (x19 < 7) {
    console.log("Bien")
} else if (x19 < 9) {
    console.log("Notable")
} else if (x19 <= 10) {
    console.log("Sobresaliente")
} else {
    console.log("Nota inexistene")
}
*/
/*
//AP ejercicio 20

let cadena = ""
let conca = ""
cadena = cadena.toLowerCase
while (cadena != "cancelar") {
    cadena = prompt("ingrese su texto, escriba cancelar para terminar")
    if (cadena != "cancelar") {
        conca = conca + "-" + cadena
    }
}
document.writeln(conca)
*/
/*
//AP ejercicio 21 - investigar NaN -

let cadena = ""
let suma = 0
console.log (suma.valueOf())
while (cadena != "cancelar") {
    cadena =(prompt("Ingrese un numero, escriba cancelar para salir"))
    if ((cadena != "cancelar") &(cadena.)){
        suma=suma+parseInt(cadena)
    }
}
*/

//AP ejercicio 22

/*
//AP ejercicio 23

let cadena=""
for (i = 1; i < 31; i++) {
    for (x = 1; x <= i; x++) {
        cadena=cadena+i
    }
    console.log(cadena)
    cadena=""
}
*/
/*
//AP ejercicio 24

let cadena = ""
let num = parseInt(prompt("Ingrese un numero"))
for (i = num; i > 0; i--) {
    for (x = 1; x <= i; x++) {
        cadena = cadena + i
    }
    console.log(cadena)
    cadena = ""
}
*/

//AP ejercicio 25

let div4 = 0
let div5 = 0
let div9 = 0
for (i = 1; i < 501; i++) {
    div4 = i % 4
    div5 = i % 5
    div9 = i % 9
    if ((div4 == 0) & (div9 != 0) & (div5 != 0)) {
        console.log(i + " es multiplo de 4")
    }// Solo multiplos de 4
    if ((div4 != 0) & (div9 != 0) & (div5 == 0)) {
        console.log(i)
        console.log("----------------")
    }//solo multiplos de 5
    if ((div4 != 0) & (div9 == 0) & (div5 != 0)) {
        console.log(i + " es multiplo de 9")
    }//solo multiplos de 9
    if ((div4 == 0) & (div9 == 0) & (div5 != 0)) {
        console.log(i + " es multiplo de 4 y de 9")
    }//solo multiplos de 4 y9
    if ((div4 == 0) & (div9 == 0) & (div5 == 0)) {
        console.log(i + " es multiplo de 4 y de 9")
        console.log("----------------")
    }//multiplos de 4 y 5
    if ((div4 == 0) & (div9 != 0) & (div5 == 0)) {
        console.log(i + " es multiplo de 4")
        console.log("----------------")
    }//multiplos de 5 y 9
    if ((div4 != 0) & (div9 == 0) & (div5 == 0)) {
        console.log(i + " es multiplo de 9")
        console.log("----------------")
    }//multiplos de 4, 5 y 9
    if ((div4 != 0) & (div5 != 0) & (div9 != 0)) {
        console.log(i)
    }
}