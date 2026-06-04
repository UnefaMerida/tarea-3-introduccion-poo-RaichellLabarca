<?php
class Especialista {
    private $db;
    private $id_especialista;
    private $nombre;
    private $rol_usuario;

    public function __construct() {
        $this->db = Conexion::getConexion();
    }

    // Registrar un nuevo especialista/usuario en el sistema
    public function registrar($nombre, $rol_usuario) {
        $sql = "INSERT INTO especialistas (nombre, rol_usuario) VALUES (:nombre, :rol);";
        $stmt = $this->db->prepare($sql);
        $stmt->bindParam(':nombre', $nombre);
        $stmt->bindParam(':rol', $rol_usuario);
        return $stmt->execute();
    }

    // Lógica de Control de Acceso (Workflow) según el rol
    public function verificarPermisos($modulo) {
        // El administrador tiene acceso absoluto a todo
        if ($this->rol_usuario === 'Administrador') {
            return true;
        }

        // El recepcionista solo accede a Admisión o Inventario
        if ($this->rol_usuario === 'Recepcionista') {
            if ($modulo === 'Admisión' || $modulo === 'Inventario') {
                return true;
            }
        }

        // Cualquier otro caso deniega el acceso
        return false;
    }

    // Cargar los datos del especialista desde la base de datos
    public function loginEspecialista($id) {
        $sql = "SELECT * FROM especialistas WHERE id_especialista = :id;";
        $stmt = $this->db->prepare($sql);
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        $resultado = $stmt->fetch(PDO::ATTR_DEFAULT_FETCH_MODE);

        if ($resultado) {
            $this->id_especialista = $resultado['id_especialista'];
            $this->nombre = $resultado['nombre'];
            $this->rol_usuario = $resultado['rol_usuario'];
            return true;
        }
        return false;
    }

    public function getRol() {
        return $this->rol_usuario;
    }
    
    public function getNombre() {
        return $this->nombre;
    }
}
?>
