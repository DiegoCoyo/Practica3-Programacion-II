import java.io.*;
import java.util.ArrayList;

public class ArchivoEmpleado {
    private String nombre;
    
    public ArchivoEmpleado(String nombre) {
        this.nombre = nombre;
    }
    
    public void crearArchivo() {
        try {
            new FileOutputStream(nombre).close();
        } catch (IOException e) {
            System.out.println("Error, no se creo el archivo.");
        }
    }
    
    public void guardarEmpleado(Empleado e) {
        try {
            FileOutputStream file = new FileOutputStream(nombre, true);
            ObjectOutputStream out;
            if (new File(nombre).length() == 0) {
                out = new ObjectOutputStream(file);
            } else {
                out = new ObjectOutputStream(file) {
                    protected void writeStreamHeader() throws IOException {
                    }
                };
            }
            out.writeObject(e);
            out.close();
            file.close();
        } catch (IOException ex) {
            System.out.println("Error, no se guardo empleado.");
        }
    }
    
    public Empleado buscaEmpleado(String n) {
        FileInputStream file = null;
        ObjectInputStream in = null;
        try {
            file = new FileInputStream(nombre);
            in = new ObjectInputStream(file);
            while (true) {
                Empleado e = (Empleado) in.readObject();
                if (e.nombre.equals(n)) {
                    return e;
                }
            }
        } catch (EOFException e) {
            return null;
        } catch (IOException | ClassNotFoundException ex) {
            System.out.println("Error, no se busco empleado.");
            return null;
        } finally {
            try {
                if (in != null) in.close();
                if (file != null) file.close();
            } catch (IOException e) {
                System.out.println("Error al cerrar el archivo.");
            }
        }
    }
    
    public Empleado mayorSalario(float sueldo) {
        Empleado mayor = null;
        FileInputStream file = null;
        ObjectInputStream in = null;
        try {
            file = new FileInputStream(nombre);
            in = new ObjectInputStream(file);
            ArrayList<Empleado> empleados = new ArrayList<>();
            while (true) {
                try {
                    Empleado e = (Empleado) in.readObject();
                    empleados.add(e);
                } catch (EOFException e) {
                    break; 
                }
            }
            for (Empleado e : empleados) {
                if (e.salario > sueldo) {
                    if (mayor == null || e.salario > mayor.salario) {
                        mayor = e;
                    }
                }
            }
        } catch (IOException ex) {
            System.out.println("Error, no se busco mayor salario: " + ex.getMessage());
        } catch (ClassNotFoundException ex) {
            System.out.println("Error no se encontro: " + ex.getMessage());
        } finally {
            try {
                if (in != null) in.close();
                if (file != null) file.close();
            } catch (IOException e) {
                System.out.println("Error al cerrar el archivo.");
            }
        }
        return mayor;
    }
}