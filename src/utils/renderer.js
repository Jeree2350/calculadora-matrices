// Comunicarse con el Backend

const API_BASE = 'http://localhost:5000';

async function testConnection() {
    try {
        const response = await fetch(`${API_BASE}/test`);
        const data = await response.json();

        console.log('Conexión exitosa:', data);
        return data;
    } catch (error) {
        console.error('Error al conectar con el backend:', error);
        return null;
    }
}

// Test inicial cuando se carga el módulo
window.addEventListener('DOMContentLoaded', async () => {
    console.log('Aplicacion carga, probando conexion al backend...');
    const connection = await testConnection();
    if (connection) {
        console.log('✅ Backend responde correctamente');
    } else {
        console.log('❌ No se pudo conectar con el backend');
    }
})