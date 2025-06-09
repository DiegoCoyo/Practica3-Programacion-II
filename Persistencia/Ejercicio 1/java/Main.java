
public class Main {
    public static void main(String[] args) {
        ArchivoEmpleado archivo = new ArchivoEmpleado("empleados.dat");
        archivo.crearArchivo();
        archivo.guardarEmpleado(new Empleado("Diego", 20, 4000.0f));
        archivo.guardarEmpleado(new Empleado("Antonio", 35, 6000.f));
        Empleado encontrado = archivo.buscaEmpleado("Diego");
        if (encontrado != null) System.out.println("Encontrado: " + encontrado.nombre + "," + encontrado.edad + "," + encontrado.salario);
        Empleado mayor = archivo.mayorSalario(5000.0f);
        if (mayor != null) System.out.println("Mayor salario: " + mayor.nombre + "," + mayor.edad + "," + mayor.salario);
    }
}
