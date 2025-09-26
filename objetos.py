class Perro:
    def __init__(self, nombre=""):
        self.nombre = nombre
    def muestra(self):
        print(f"Soy {self.nombre}")

p = Perro("Firulais")
#p.nombre = "Firulais"
p.muestra()

"""
class Perro{
    public string Nombre {get; set;}
    public Perro(string nombre){
        this.Nombre = nombre;
    }
    public void Muestra(){
        Console.WriteLine($"Soy {Nombre}")
    }
}
"""