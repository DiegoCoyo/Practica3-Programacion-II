public class Main {
    public static void main(String[] args) {

        Pila <Integer> pilaNum = new Pila<Integer>();
        pilaNum.apilar(1);
        pilaNum.apilar(2);
        pilaNum.apilar(3);

        System.out.println("Pila 1:");
        pilaNum.mostrar();
        System.out.println("Desapilado: " + pilaNum.desapilar());
        System.out.println("Despues de desapilar:");
        pilaNum.mostrar();
        
        Pila <String> pilaTexto = new Pila<String>();
        pilaTexto.apilar("uno");
        pilaTexto.apilar("dos");
        pilaTexto.apilar("tres");
        System.out.println("Pila 2:");
        pilaTexto.mostrar();
        System.out.println("Desapilado: " + pilaTexto.desapilar());
        System.out.println("Despues de desapilar:");
        pilaTexto.mostrar();
    }
}