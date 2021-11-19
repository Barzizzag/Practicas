package UTN;

public class Car {
    private Integer velocidadMax;
    private String modelo;
    private String color;
/*
    public void mostrarColor(){
        System.out.println("Mi color es: "+color);
    }
    public double getVelocidadMaxMillas(){
        Double velocidadMaxMillas;
        velocidadMaxMillas=velocidadMax*0.6213;
        return velocidadMaxMillas;
    }
    public void setVelocidadMax(Integer velocidadMax){
        if (velocidadMax>400){
            System.out.println("Seguro que es un auto?");
        }else{
            this.velocidadMax=velocidadMax;
        }
    }
    public void setColor(String color){
        if (color=="Amarillo"){
            System.out.println("Ese color no esta permitido");
            this.color="Azul";
        }else {
            this.color=color;
        }
    }
    public Integer getVelocidadMaxKm(){
        return velocidadMax;
    }
    public String getColor(){
        return color;
    }
    public Integer getVelocidadMax() {
        return velocidadMax;
    }
    public String getModelo() {
        return modelo;
    }
    public void setModelo(String modelo) {
        this.modelo = modelo;
    }*/
    public void setColor(String color){
        this.color=color;
    }
    public void setColor(String color1, String color2){
        this.color=color1+" "+color2;
    }
    public String getColor(){
        return color;
    }
}
