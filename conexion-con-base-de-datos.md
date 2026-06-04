<?php
class Conexion {
    private static $instance = null;
    private $pdo;

    private function __construct() {
        try {
            // Se conecta o crea la base de datos SQLite en el mismo directorio
            $this->pdo = new PDO("sqlite:osgi_cae.db");
            $this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            $this->crearTablas();
        } catch (PDOException $e) {
            die("Error en la conexión: " . $e->getMessage());
        }
    }

    public static function getConexion() {
        if (self::$instance == null) {
            self::$instance = new Conexion();
        }
        return self::$instance->pdo;
    }

    private function crearTablas() {
        // Tabla de Especialistas / Usuarios para el Control de Acceso
        $sqlEspecialistas = "CREATE TABLE IF NOT EXISTS especialistas (
            id_especialista INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            rol_usuario TEXT NOT NULL
        );";

        // Tabla de Admisión y Registro (Pacientes)
        $sqlAdmision = "CREATE TABLE IF NOT EXISTS admision_registro (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_paciente TEXT NOT NULL,
            nivel_prioridad TEXT NOT NULL,
            motivo_consulta TEXT NOT NULL,
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );";

        $this->pdo->exec($sqlEspecialistas);
        $this->pdo->exec($sqlAdmision);
    }
}
?>
