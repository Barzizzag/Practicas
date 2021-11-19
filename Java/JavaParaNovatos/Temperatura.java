package JavaParaNovatos;
class Temperatura{
    private double celsius;
    private double farenheit;
    public double aCelsius (double temp){
        celsius =(temp-32)/1.8;
        return (celsius);
    }
    public double aFarenheit (double temp){
        farenheit = 1.8 * temp + 32;
        return (farenheit);
    }
}