public class Main {
    public static void main(String[] args) {
        Catalogo<Libro> libros = new Catalogo<Libro>();
        libros.agregar(new Libro("Mñana llovera", "San Diego"));
        libros.agregar(new Libro("Morir o Vivir", "Dante Gabriel"));
        System.out.println(libros.buscar(0));
        System.out.println(libros.buscar(1));
        
        Catalogo<Producto> productos = new Catalogo<Producto>();
        productos.agregar(new Producto("Tablet", 2100.0));
        productos.agregar(new Producto("Television", 6200.0));
        System.out.println(productos.buscar(0));
        System.out.println(productos.buscar(1));
    }
}