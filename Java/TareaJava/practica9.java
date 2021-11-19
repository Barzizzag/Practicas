package TareaJava;

import java.util.Scanner;

public class practica9 {
    // Ejercicio 1
    /*
     * public static void main(String []args){ System.out.print
     * ("Ingrese el ancho del terreno: "); Float ladoX=new
     * Scanner(System.in).nextFloat();
     * System.out.print("Ingrese el largo del terreno: "); Float ladoY=new
     * Scanner(System.in).nextFloat(); Float superficie =ladoX*ladoY;
     * System.out.print("La superficie del terreno es: "+superficie); }
     */
    // Ejercicio 2
    /*
     * public static void main(String []args){ System.out.print
     * ("Ingrese el primer numero: "); Float nro1 = new
     * Scanner(System.in).nextFloat(); System.out.print
     * ("Ingrese el segundo numero: "); Float nro2 = new
     * Scanner(System.in).nextFloat(); float suma = nro1+nro2; float rest =
     * nro1-nro2; float mult = nro1*nro2; float divi = nro1/nro2; System.out.println
     * ("La suma vale "+suma+" la resta es "+rest+" la multiplicacion "
     * +mult+" y la division "+divi); }
     */
    //Ejercicio 3
    /*
    public static void main(String[]args){
        System.out.print("Ingrese la altura en metros: ");
        Float alto=new Scanner(System.in).nextFloat();
        System.out.print("Ingrese el ancho en metros: ");
        Float  ancho=new Scanner(System.in).nextFloat();
        Float rendimiento=3.6f;
        Float superficie=ancho*alto;
        Float pinturaNecesaria=superficie/rendimiento;
        System.out.println("Seran necesarios "+pinturaNecesaria+" litros de pintura");
    }*/
    //Ejercicio 4
    /*
    static public void main (String[]args){
        System.out.print("Ingrese la variable a: ");
        String a = new Scanner(System.in).next();
        System.out.print("Ingrese la variable b: ");
        String b= new Scanner(System.in).next();
        String aux=b;
        b=a;
        a=aux;
        System.out.print("Las variables fueron cambiadas, ahora b vale: "+b+" y a vale: "+a);
    }*/
    //Ejercicio 5
    /*
    public static void main(String[]args){
        System.out.print("Ingrese el perimetro del cuadrado: ");
        double perimetro=new Scanner(System.in).nextDouble();
        double lado=perimetro/4;
        double volumen=lado*lado*lado;
        System.out.print("El volumen del cubo de lado "+lado+" es "+volumen);
    }*/
    //Ejercicio 6
    /*
    public static void main(String[]args){
        double acumulado=0;
        for (int i=1; i<=5; i++){
            System.out.print("Ingrese el precio del articulo: ");
            double precioUnitario = new Scanner (System.in).nextDouble();
            System.out.print("Ingrese la cantidad vendida: ");
            int cantidad= new Scanner (System.in).nextInt();
            double precioTotal  = cantidad*precioUnitario;
            System.out.println ("El valor vendido de articulo "+i+" es:"+precioTotal);
            acumulado=acumulado+precioTotal;
        }
        System.out.print("El total vendido es: "+acumulado);
    }*/
    //Ejercicio 7
    /*
    public static void main (String[]args){
        System.out.print("Ingrese un numero: ");
        double numero =new Scanner(System.in).nextDouble();
        double par=numero%2;
        if (par == 0){
            System.out.print(numero+" es par.");
        } else{
            System.out.print(numero+" es impar.");
        }
    }*/
    //Ejercicio 8
    /*
    public static void main (String []args){
        System.out.print ("Ingrese un numero: ");
        int numero= new Scanner (System.in).nextInt();
        if (numero%2==0){
            System.out.print("El numero ingresado es multiplo de dos");
        }else {
            System.out.print ("El numero ingresado no es multiplo de dos");
        }
    }*/
    //Ejercicio 9
    /*
    public static void main(String[]args){
        System.out.print("Ingrese un numero: ");
        int numero=new Scanner (System.in).nextInt();
        if (numero%3==0){
            System.out.print("El numero "+numero+" es multiplo de 3");
        }else {
            System.out.print("El numero "+numero+" no es multiplo de 3");
        }
    }*/
    //Ejercicio 10
    /*              Este ejercicio esta mal!!!!!!!!!!!
    public static void main (String []args){
        System.out.print("Ingrese un numero menor a 100: ");
        int numero = new Scanner(System.in).nextInt();
        if (numero<=100){
            if (numero%2==0){
                System.out.print("El numero no es primo");
            }else if(numero%3==0){
                System.out.print("El numero no es primo");
            }else if(numero%5==0){
                System.out.print("El numero no es primo");
            }else if (numero%7==0){
                System.out.print ("El numero no es primo");
            }else{
                System.out.print("El numero "+numero+" es primo");
            }
        }else{
            System.out.print("El numero ingresado esta fuera del rango");
        }
    }//Acá hay que seguir trabajando
    public static void main (String [] args){
        Scanner sc =new Scanner (System.in);
        System.out.print ("Ingrese un numero del 1 al 100: ");
        double numero= sc.nextDouble();
        boolean primo=false;
        if ((numero<=0)||(numero==1)){//Atajamos que manden un uno o un cero
            System.out.print ("Dije del 1 al 100; por convencion el 1 no se considera primo");
        }
        for (int i=1; i<numero ;i++){//buscamos primos por encima de dos
            double divisible=numero%i;
            System.out.println(i+" "+divisible);
            if (divisible!=0){
                primo=true;
                
            }
        }
        System.out.print(numero+ " es primo "+primo);
        
    }*/
    //Ejercicio 11
    /*
    public static void main (String []args){
        System.out.print ("Ingrese el Sueldo basico: ");
        double basico= new Scanner (System.in).nextDouble();
        System.out.print ("Ingrese la categoria: ");
        int categoria = new Scanner (System.in).nextInt();
        switch(categoria){
            case (1):
                basico=basico*0.7;
                break;
            case (2):
                basico=basico*0.75;
                break;
            case (3):
                basico=basico*0.75;
                break;
            case (4):
                basico=basico*0.10;
                break;
            default://Sin descuento
                break;
        }
        System.out.print ("El sueldo neto es: "+basico+" y la categoria es: "+categoria);
    }*/
    //Ejercicio 12
    /*
    public static void main (String [] args){
        Scanner sc = new Scanner (System.in);
        int numero=0;
        do{
            System.out.print("Ingrese un numero del 1 al 7: ");
            numero = sc.nextInt();
        }while ((numero<=0) || (numero>=8 ));
        switch(numero){
            case(1):
                System.out.print("Hoy es lunes");
                break;
            case(2):
                System.out.print("Hoy es martes");
                break;
            case(3):
                System.out.print("Hoy es miercoles");
                break;
            case(4):
                System.out.print("Hoy es jueves");
                break;
            case(5):
                System.out.print("Hoy es viernes");
                break;
            case(6):
                System.out.print("Hoy es sabado");
                break;
            case(7):
                System.out.print("Hoy es domingo");
                break;
            default:
                System.out.print("No se como llegamos acá!!");
        }
    }*/
    //Ejercicio 13
    /*
    public static void main (String []args){
        Scanner sc= new Scanner(System.in);
        int mayores=0;
        for (int i=0;i<15; i++){
            System.out.print ("Ingrese un numero: ");
            int numero = sc.nextInt();
            if (numero>100){
                mayores+=1;
            }
        }
        System.out.print("Hay "+mayores+" numeros mayores a cien.");
    }*/
    //Ejercicio 14
    /*
    public static void main (String []args){
        Scanner sc = new Scanner (System.in);
        int mayores = 0;
        for (int i=0; i<49; i++){
            System.out.print("Ingrese un numero: ");
            int numero = sc.nextInt();
            if (numero>10){
                mayores +=1;
            }
        }
        System.out.print("La cantidad de numeros mayores a 10 es: "+mayores);
    }*/
    //Ejercicio 15
    /*
    public static void main (String[]args){
        Scanner sc = new Scanner (System.in);
        int validos = 0;
        for (int i=0; i<19;i++ ){
            System.out.println("Ingrese un numero: ");
            int numero = sc.nextInt();
            if (numero>50 && numero<100 && numero%2==0){
                validos+=1;
            }
        }
        System.out.print("La cantidad de mayores de 50, menores a 100 y pares es:"+validos);
    }*/
}
