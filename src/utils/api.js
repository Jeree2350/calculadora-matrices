export async function calcularMatriz(filas, columnas) {
  const response = await fetch("http://localhost:8000/calcular", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ filas, columnas }),
  });

  return await response.json();
}
