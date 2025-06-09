
public class Main {
    public static void main(String[] args) {
        ArchivoCliente archivo = new ArchivoCliente("clientes.dat");
        archivo.crearArchivo();
        archivo.guardaCliente(new Cliente(1, "Miguel", 74392250));
        archivo.guardaCliente(new Cliente(2, "Jonatan", 78392112));
        Cliente encontradoID = archivo.buscarCliente(1);
        if (encontradoID != null) System.out.println("Encontrado por ID: " + encontradoID.id + "," + encontradoID.nombre + "," + encontradoID.telefono);
        Cliente encontradoCelular = archivo.buscarCelularCliente(74392250);
        if (encontradoCelular != null) System.out.println("Encontrado por Celular: " + encontradoCelular.id + "," + encontradoCelular.nombre + "," + encontradoCelular.telefono);
    }
}