const inputTitulo = document.getElementById("tituloCard");
const botaoCriar = document.getElementById("criarCard");
const cardsContainer = document.getElementById("cardsContainer");

botaoCriar.addEventListener("click", function() {

    const titulo = inputTitulo.value;

    if (titulo.trim() === "") {
        alert("Digite um título!");
        return;
    }

    const card = document.createElement("div");

    const tituloCard = document.createElement("h3");
    tituloCard.textContent = titulo;

    const botaoRemover = document.createElement("button");
    botaoRemover.textContent = "Remover";

    botaoRemover.addEventListener("click", function() {
        card.remove();
    });

    card.appendChild(tituloCard);
    card.appendChild(botaoRemover);

    cardsContainer.appendChild(card);

    inputTitulo.value = "";
});