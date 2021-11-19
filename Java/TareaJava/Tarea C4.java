package TareaJava;

import java.util.Scanner;

class nroPar{
    public static void main(String[] args){
        System.out.print("Ingrese un numero: ");
        int numero =0;
        Scanner numIng= new Scanner (System.in);
        numero =numIng.nextInt();
        int par=(numero%2);
        if (par==0){
            System.out.println (numero + " es par");
        }else{
            System.out.println (numero + " es impar");
        }
    }
}

class nroPar2{
    public static void main(String[] args){
        System.out.print("Ingrese un numero: ");
        int numero =0;
        Scanner numIng= new Scanner (System.in);
        numero =numIng.nextInt();
        int par=(numero%2);
        if (par==0){
            System.out.println (numero + " es par");
        }else{
            System.out.println (numero + " es impar");
        }
    }
}
//-------------------------------------------------------
class bancos{
    public static void main (String [] args){
        System.out.print ("Ingrese el numero de alumnos: ");
        int cantAlum=0;
        Scanner scannerAlumnos= new Scanner(System.in);
        cantAlum =scannerAlumnos.nextInt();
        System.out.print ("Ingrese la cantidad de bancos: ");
        //int cantBancos=0
        //Scanner scannerBancos= new Scanner (System.in);
        //cantBancos =scannerBancos.nextInt();
        int cantBancos= (new Scanner (System.in)).nextInt(); //Es lo mismo que lo de arriba ¿?
        if (cantAlum<=cantBancos){
            System.out.println ("Hay bancos suficientes para todos los alumnos");
        }else {
            int falta=(cantAlum-cantBancos);
            System.out.println("Faltan "+ falta+" bancos");
        }
    }
}
//-------------------------------------------------------
class descuento{
    public static void main (String[]args){
        
        float costoFinal=000;
        System.out.print("Ingrese el valor de la compra: ");
        float costo=(new Scanner(System.in)).nextFloat();
        System.out.print("Ingrese la forma de pago: ");
        String foPago=(new Scanner(System.in)).next();
        if (foPago.equals("contado")){
            costoFinal=0.9f*costo;
            System.out.println ("El valor de la compra con descuento es: "+costoFinal);
        }else{
            System.out.println("El medio de pago elegido no tiene descuento");
        }
    }
}
//-------------------------------------------------------
class semana{
    public static void main (String []args){
        System.out.print("Ingrese el día de la semana: ");
        int dia=(new Scanner(System.in)).nextInt();
        switch (dia){
            case 1:
                System.out.print("Hoy es lunes");
                break;
            case 2:
                System.out.print("Hoy es martes");
                break;
            case 3:
                System.out.print("Hoy es miercoles");
                break;
            case 4:
                System.out.print("Hoy es jueves");
                break;
            case 5:
                System.out.print("Hoy es viernes");
                break;
            case 6:
                System.out.print("Hoy es sabado");
                break;
            case 7:
                System.out.print("Hoy es domingo");
                break;
            default:
                System.out.print("No corresponde a ningun día");
        }
    }
}
//-------------------------------------------------------
class tablas{
    public static void main(String[]args){
        System.out.print("Que tabla quieres conocer: ");
        int tabla=(new Scanner(System.in)).nextInt();
        System.out.print("Hasta que numero: ");
        int hasta=(new Scanner(System.in)).nextInt();
        boolean condicion=true;
        int i=1;
        int multi=0;
        while (condicion){
            multi=tabla*i;
            System.out.println(tabla+" X "+i+" = "+multi);
        if (i>=hasta){
            condicion=false;
        }
        i++;
        }
    }
}
//-------------------------------------------------------
class tabla2{
    public static void main (String[]args){
        boolean otro=true;
        do{
            int multi=0;
            int contador=1;
            boolean ciclo=true;
            System.out.print("Que tabla desea saber: ");
            int tabla =(new Scanner(System.in)).nextInt();
            System.out.print("Hasta que numero: ");
            int hasta =(new Scanner(System.in)).nextInt();
            do{
                multi= contador*tabla;
                System.out.println(tabla +" X "+contador + " = "+multi);
                contador++;
                if (hasta<contador){
                    ciclo=false;
                }
            }while (ciclo);
            System.out.print("Desea continuar si/no: ");
            String sigue=(new Scanner(System.in)).next();
            if (sigue.equalsIgnoreCase("no")){
                otro=false;
            }
        } while (otro);
    }
}
//-------------------------------------------------------
class cicloPara{
    public static void main (String []args){
        float acumulador=0f;
        float promedio=0f;
        for (int i=0; i<4; i++){
            System.out.print("Ingrese un numero: ");
            float numero= (new Scanner(System.in)).nextFloat();
            acumulador=acumulador+numero;
        }
        promedio=acumulador/4;
        System.out.print("El promedio de los numeros es: "+promedio);
    }
}
