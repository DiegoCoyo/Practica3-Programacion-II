public class Main {
    public static void main(String[] args) {
        Caja <Integer> numero = new Caja<Integer>();
        numero.guardar(2387);
        System.out.println(numero.obtener());
        
        Caja <String> texto = new Caja<String>();
        texto.guardar("Como estas Hoy");
        System.out.println(texto.obtener());
    }
}