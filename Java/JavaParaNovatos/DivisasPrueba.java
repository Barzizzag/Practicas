package JavaParaNovatos;

public class DivisasPrueba {
    public static void main (String[]args){

        double dinero=100;
        Divisas div = new Divisas();
        System.out.println(div.aDolar(dinero));
        System.out.println(div.aPesos(dinero));
        double taza = 1.24;
        Divisas div2 = new Divisas(taza);
        System.out.println(div2.aDolar(dinero));
        System.out.println(div2.aPesos(dinero));

    }
}
