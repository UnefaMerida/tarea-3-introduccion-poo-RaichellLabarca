<?php
class Admision {
    private $db;

    public function __construct() {
        $this->db = Conexion::getConexion();
    }

    // Registrar un paciente en el sistema (Entrada del Workflow)
    public function registrarPaciente($nombre, $nivel_prioridad, $motivo_consulta) {
        $sql = "INSERT INTO admision_registro (nombre_paciente, nivel_prioridad, motivo_consulta) 
                VALUES (:nombre, :prioridad, :motivo);";
        $stmt = $this->db->prepare($sql);
        $stmt->bindParam(':nombre', $nombre);
        $stmt->bindParam(':prioridad', $nivel_prioridad);
        $stmt->bindParam(':motivo', $motivo_consulta);
        return $stmt->execute();
    }

    // Listar pacientes ordenados por prioridad o entrada para el DSS (Procesamiento)
    public function listarPacientes() {
        $sql = "SELECT * FROM admision_registro ORDER BY 
                CASE nivel_prioridad 
                    WHEN 'Alta' THEN 1 
                    WHEN 'Media' THEN 2 
                    WHEN 'Baja' THEN 3 
                    ELSE 4 
                END, fecha_registro ASC;";
        $stmt = $this->db->query($sql);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
}
?>
