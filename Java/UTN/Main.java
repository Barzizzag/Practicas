package UTN;
public class Main{

    public static void main (String []args){
        Car myCar= new Car();
        Car anotherCar = new Car();

        //myCar.velocidadMax=null;
        //anotherCar.velocidadMax=220;

        //System.out.println(myCar.velocidadMax);
        //System.out.println(anotherCar.velocidadMax);
        //myCar.setVelocidadMax(100);
        //anotherCar.setVelocidadMax(560);
        myCar.setColor("Amarillo");
        System.out.println(myCar.getColor());
        myCar.setColor("Rojo", "Blanco");
        System.out.println(myCar.getColor());
    }

}