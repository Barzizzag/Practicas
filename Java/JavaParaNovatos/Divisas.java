package JavaParaNovatos;
class Divisas{
    double tasaDeConv;
    Divisas(){
        tasaDeConv=98.28;
    }
    Divisas(double tasa){
        tasaDeConv=tasa;
    }
    double aDolar(double dinero){
        dinero=dinero/tasaDeConv;
        return dinero;
    }
    double aPesos(double dinero){
        dinero=dinero*tasaDeConv;
        return dinero;
    }
}