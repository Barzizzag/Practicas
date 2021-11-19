console.log("Acá comienza el TP2")
/*
//AP funcion 1

let num = 0
function saludo(num) {
    for (i = 0; i < num; i++) {
        console.log("Bienvenidos al curso Full Stack")
    }
}
num = parseInt(prompt("Ingrese un numero"))
saludo(num)
*/
/*
//AP funcion 2

function maximo(x, y) {
    if (x > y) {
        console.log("El primer numero es el mayor")
    } else {
        console.log("El segundo numero es el mayor")
    }
}
x = parseInt(prompt("Ingrese el primer numero"))
y = parseInt(prompt("Ingrese el segundo numero"))
maximo(x, y)
*/
/*
//AP funcion 3

function promedio3(x, y, z) {
    let prom = (x + y + z) / 3
    console.log(prom)
}
x = parseInt(prompt("Ingrese el primer numero"))
y = parseInt(prompt("Ingrese el segundo numero"))
z = parseInt(prompt("Ingrese el tercer numero"))
promedio3(x, y, z)
*/
/*
//AP funcion 4

var x = 0
var acumulador = 0
var contador = 0
var prom = 0
function leer() {
    while (x != -1) {
        x = parseFloat(prompt("Ingrese un numero"))
        if (x != -1) {
            acumulador = acumulador + x
            contador += 1
        }
    }
}
leer()
prom = acumulador / contador
console.log("El promedio es: " + prom)
*/
/*
//AP funcion 5

var x5=0
var dbl=0
console.log("llegamos a funcion doble")
function doble(x5){
    dbl=x5*2
    return dbl
}
x5=parseInt(prompt("Ingrese el valor para obtener su doble"))
var resultado= doble (x5)
console.log(resultado)
*/
/*
//AP funcion 6

var x6=0
var cuad=0
function cuadrado (x6){
    return x6*x6
}
x6=parseInt(prompt("Ingrese un valor para obtener el cuadrado"))
console.log("El cuadrado es: "+(cuad =cuadrado(x6)))
*/
/*
// AP funcion 7

console.log("Llegamos a funcion siguiente")
var x7=0
var sig=0
var dob=0
function siguiente(x7){
    let x=parseInt(x7)
    return (x+1) 
}
x7 = parseInt(prompt("Ingrese el valor del ejercicio 7"))
sig=siguiente(x7)
dob=doble(x7)
cuad=cuadrado(x7)
console.log ("El siguiente numero es: "+ sig + "El doble es: " + dob + "Y su cuadrado es: " + cuad)
*/
/*
//AP funcion 8

x8=0
dobsig=0
console.log("Llegamos a funcion doble siguiente")
function doblesig(x8){
    dobsig=siguiente(x8)
    dobsig=doble(dobsig)
    return dobsig
}
x8=parseInt(prompt("Ingrese el valor del ejercicio 8"))
doblesig(x8)
console.log("El doble del siguiente es: "+ dobsig)
*/
//AP funcion 9
/*
x9=0
dobSigCuad=0
function dsCuadrado(x9){
    dobSigCuad=doblesig(x9)
    dobSigCuad=cuadrado(dobSigCuad)
    return dobSigCuad
}
x9=parseInt(prompt("Ingrese el numero del ej 9"))
dsCuadrado(x9)
console.log("El cuadrado del doble del siguiente es: "+ dobSigCuad)
*/
/*
//AP ejercicio 10

lado = 0
peri = 0
function perimetro(lado) {
    peri = lado * 4
    return peri
}
lado = parseInt(prompt("Ingrese el lado del cuadrado"))
//perimetro(lado)
//console.log("El perimetro es:" + peri)

//AP ejercicio 11
supe=0
function superf(lado){
    supe=lado*lado
    return supe
}
superf(lado)
console.log("La superficie es:"+ supe)
*/
/*
//AP Ejercicio 12

pi = Math.PI
radio = 0
circunferencia = 0
function circun(radio) {
    circunferencia = 2 * pi * radio
    return circunferencia
}
radio = parseFloat(prompt("Ingrese el radio"))
//circun(radio)
//console.log("La circunferencia es:" + circunferencia)

//AP Ejercicio 13
are = 0
function area(radio) {
    are = pi * radio * radio
    return are
}
area(radio)
console.log("El area del circulo es: " + are)
*/
/*
//AP Ejercicio 14

mes = 0
dias = 0
function funcionMes(mes) {
    if ((mes == 1) | (mes == 3) | (mes == 5) | (mes == 7) | (mes == 8) | (mes == 10) | (mes == 12)) {
        dias = 31
    } else if (mes == 2) {
        dias = 28
    } else {
        dias = 30
    }
    return dias
}
mes=parseInt(prompt("Ingrese el numero del mes"))
funcionMes(mes)
console.log("El mes elegido tiene: " + dias + " dias")
*/
/*
//AP ejercicio 15

let anio=0
let bisiesto=false
function funBis(anio){
    if (((anio%4)==0)&((anio%100)==0)&((anio%400)==0)){
       bisiesto=true
    }else if (((anio%4)==0)&((anio%100)!=0)&((anio%400)!=0)){
        bisiesto=true
    }else {
        bisiesto=false
    }
    return bisiesto
}
anio=parseInt(prompt("Ingrese un año"))
funBis(anio)
if (bisiesto==true){
    console.log("Es un año bisiesto")
}else{
    console.log("No es un año bisiesto")
}
*/
/*
//AP ejercicio16

let bisiesto = false;
let dia = 0;
let mes = 0;
let anio = 0;

function funBis(anio) {
    if (((anio % 4) == 0) & ((anio % 100) == 0) & ((anio % 400) == 0)) {
        bisiesto = true
    } else if (((anio % 4) == 0) & ((anio % 100) != 0) & ((anio % 400) != 0)) {
        bisiesto = true
    } else {
        bisiesto = false
    }
    console.log("func bisiesto: " + bisiesto)
    return bisiesto
}

function diaAnterior() {
    dia = parseInt(prompt("ingrese el dia"));
    mes = parseInt(prompt("Ingrese el mes"));
    anio = parseInt(prompt("Ingrese el año"));
    bisiesto = funBis(anio);
    console.log("Fecha inicial: " + dia + "/" + mes + "/" + anio + " Es bisiesto: "  bisiesto)
    //Controlo que los dias en el mes existe o los pido nuevamente.
    if (((mes == 4) || (mes == 6) || (mes == 9) || (mes == 11)) && (dia > 30)) {
        console.log("El mes " + mes + " no tiene " + dia + " dias");
        dia = parseInt(prompt("ingrese el dia"));
    } else if (((mes == 2) && (dia > 28)) && (bisiesto == false)) {
        console.log("Febrero no tiene mas de 28 dias, no es año bisisesto");
        dia = parseInt(prompt("ingrese el dia"));
    } else if (((mes == 2) && (dia > 29)) && (bisiesto == true)) {
        console.log("Febrero no puede tener mas de 29 dias");
        dia = parseInt(prompt("ingrese el dia"));
    } else if (((mes == 1) || (mes == 3) || (mes == 5) || (mes == 7) || (mes == 8) || (mes == 10) || (mes == 12)) && (dia > 31)) {
        console.log("El mes " + mes + " no tiene " + dia + " dias");
        dia = parseInt(prompt("ingrese el dia"));
    } else { }

    if (dia == 1) {//Primero de cualquier mes, cambia mes
        mes = mes - 1
        if (mes == 0) {//Acá para el primero de enero, cambia año
            anio = anio - 1
            mes = 12
        }
        if ((mes == 4) || (mes == 6) || (mes == 9) || (mes == 11)) {
            dia = 30
        } else if ((mes == 1) || (mes == 3) || (mes == 5) || (mes == 7) || (mes == 8) || (mes == 10) || (mes == 12)) {
            dia = 31
        } else if ((mes == 2) && (bisiesto == false)) {
            dia = 28
        } else if ((mes == 2) && (bisiesto == true)) {
            dia = 29
        } else { }
    } else {//Solo cambia el dia
        dia = dia - 1
    }
    return (dia, mes, anio, bisiesto)
}

diaAnterior();
console.log("Nueva fecha:  " + dia + "/" + mes + "/" + anio)
*/

//AP ejercicio  17
let bisiesto = false;
let dia = 0;
let mes = 0;
let anio = 0;

function funBis(anio) {
    if (((anio % 4) == 0) & ((anio % 100) == 0) & ((anio % 400) == 0)) {
        bisiesto = true
    } else if (((anio % 4) == 0) & ((anio % 100) != 0) & ((anio % 400) != 0)) {
        bisiesto = true
    } else {
        bisiesto = false
    }
    console.log("func bisiesto: " + bisiesto)
    return bisiesto
}

function ultimoDia() {
    dia = parseInt(prompt("ingrese el dia"));
    mes = parseInt(prompt("Ingrese el mes"));
    anio = parseInt(prompt("Ingrese el año"));
    bisiesto = funBis(anio);
    console.log("Fecha inicial: " + dia + "/" + mes + "/" + anio + "/" + bisiesto)
    //Controlo que los dias en el mes existe o los pido nuevamente.
    if (((mes == 4) || (mes == 6) || (mes == 9) || (mes == 11)) && (dia > 30)) {
        console.log("El mes " + mes + " no tiene " + dia + " dias");
        dia = parseInt(prompt("ingrese el dia"));
    } else if (((mes == 2) && (dia > 28)) && (bisiesto == false)) {
        console.log("Febrero no tiene mas de 28 dias, no es año bisisesto");
        dia = parseInt(prompt("ingrese el dia"));
    } else if (((mes == 2) && (dia > 29)) && (bisiesto == true)) {
        console.log("Febrero no puede tener mas de 29 dias");
        dia = parseInt(prompt("ingrese el dia"));
    } else if (((mes == 1) || (mes == 3) || (mes == 5) || (mes == 7) || (mes == 8) || (mes == 10) || (mes == 12)) && (dia > 31)) {
        console.log("El mes " + mes + " no tiene " + dia + " dias");
        dia = parseInt(prompt("ingrese el dia"));
    } else { }

    if ((mes == 4) || (mes == 6) || (mes == 9) || (mes == 11)) {
        dia = 30
    } else if ((mes == 1) || (mes == 3) || (mes == 5) || (mes == 7) || (mes == 8) || (mes == 10) || (mes == 12)) {
        dia = 31
    } else if ((mes == 2) && (bisiesto == false)) {
        dia = 28
    } else if ((mes == 2) && (bisiesto == true)) {
        dia = 29
    } else { }
    //Este switch no me esta andando.
    /*switch (mes) {
        case ((mes == 1) || (mes == 3) || (mes == 5) || (mes == 7) || (mes == 8) || (mes == 10) || (mes == 12)):
            dia = 31;
            break;
        case ((mes == 4) || (mes == 6) || (mes == 9) || (mes == 11)):
            dia = 30;
            break;
        case ((mes == 2) && (bisiesto == false)):
            dia = 28
            break;
        case ((mes == 2) && (bisiesto == true)):
            dia = 29
            break;
        default:
    }*/
    return (dia)
}
ultimoDia();
console.log("El ultimo dia del mes " + mes + " es " + dia)