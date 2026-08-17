// Variáveis numéricas
let precoProduto = 20;
let quantidade = 3;

// Cálculos
let total = precoProduto * quantidade;
let dobro = total * 2;
let resto = total % 2;

// Variáveis booleanas
let cupomValido = true;
let freteGratis = false;

// Operadores lógicos
let algumBeneficio = cupomValido || freteGratis;
let todosBeneficios = cupomValido && freteGratis;

// Mostrar no console
console.log("Preço do produto:", precoProduto);
console.log("Quantidade:", quantidade);
console.log("Total da compra:", total);
console.log("Dobro do total:", dobro);
console.log("Resto da divisão por 2:", resto);

console.log("Cupom válido:", cupomValido);
console.log("Frete grátis:", freteGratis);
console.log("Algum benefício (OU):", algumBeneficio);
console.log("Todos os benefícios (E):", todosBeneficios);

// Mostrar os resultados na página
document.getElementById("preco").textContent = "R$ " + precoProduto;
document.getElementById("quantidade").textContent = quantidade;
document.getElementById("total").textContent = "R$ " + total;
document.getElementById("dobro").textContent = "R$ " + dobro;
document.getElementById("resto").textContent = resto;

document.getElementById("cupom").textContent = cupomValido;
document.getElementById("frete").textContent = freteGratis;
document.getElementById("algum").textContent = algumBeneficio;
document.getElementById("todos").textContent = todosBeneficios;