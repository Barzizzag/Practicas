package TareaJava;

import java.util.Scanner;
public class Burbuja{
public static void main (String []args){
    Scanner sc =new Scanner(System.in);
    int ordOk=0;
    boolean ordenado=false;
    //Hacemos el ingreso de los numeros.
    System.out.print("Ingrese la cantidad de numeros a ordenar: ");
    int n=sc.nextInt();
    int  aOrdenar[]= new int[n];
    for (int x=0; x<aOrdenar.length; x++){
        System.out.print("Numero: "); 
        aOrdenar[x]=sc.nextInt();
    }
    //Acá comienza el ordenar.
    while (ordenado==false){
        for (int i=0; i<(aOrdenar.length-1); i++){
            if (aOrdenar[i]>aOrdenar[i+1]){
                int aux=aOrdenar[i];
                aOrdenar[i]=aOrdenar[i+1];
                aOrdenar[i+1]=aux;
                ordOk-=1;
            }else {
                ordOk+=1;
            }  
        }
        if (ordOk>=aOrdenar.length){
            ordenado=true;
        }

    }
    //Imprimo vector ordenado.
    for (int y=0; y<aOrdenar.length;y++){
        System.out.print(aOrdenar[y]+", ");
    }
}
}