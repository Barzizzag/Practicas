package TareaJava;

public class Fibonacci {
    public static void main(String args[]) {
      int x0=0;
      int x1=1;
      int acumulador=0;
      boolean b1=true;
      //Como los dos primeros numeros se imprimen desde adentro del if, solo iteramos hasta el 8
      for (int i=0; i<8; i++){
          //imprimimos los dos primeros terminos de la serie
          if (b1==true){
              System.out.print(x0 + " , " + x1);
              b1=false;
          }
          // Imprimimos los terminos siguientes
          acumulador= x0+x1;
          x0=x1;
          x1=acumulador;
          System.out.print(" , "+acumulador);
      }
    }
}