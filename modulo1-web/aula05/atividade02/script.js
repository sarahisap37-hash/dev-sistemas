const botao = document.getElementById("buscar");
const cidade = document.getElementById("cidade");
const resultado = document.getElementById("resultado");

botao.addEventListener("click", function () {

    // Pega as coordenadas da cidade selecionada
    const coordenadas = cidade.value.split(",");

    const lat = coordenadas[0];
    const lon = coordenadas[1];

    // Pega o nome da cidade selecionada
    const nomeCidade = cidade.options[cidade.selectedIndex].text;

    // Monta a URL da API
    const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`;

    // Faz a requisição
    fetch(url)
        .then(resposta => resposta.json())
        .then(data => {

            // Pega a temperatura atual
            const temperatura = data.current_weather.temperature;

            // Escolhe o ícone de acordo com a temperatura
            let icone;

            if (temperatura < 15) {
                icone = "❄️";
            } else if (temperatura < 25) {
                icone = "🌤️";
            } else {
                icone = "☀️";
            }

            // Altera o fundo de acordo com a temperatura
            if (temperatura < 15) {
                document.body.style.background =
                    "linear-gradient(180deg, #2196f3, #90caf9)";
            } else if (temperatura < 25) {
                document.body.style.background =
                    "linear-gradient(180deg, #78909c, #cfd8dc)";
            } else {
                document.body.style.background =
                    "linear-gradient(180deg, #ff9800, #f44336)";
            }

            // Mostra os dados na tela
            resultado.innerHTML = `
                <h2>${nomeCidade}</h2>

                <div style="font-size: 60px;">
                    ${icone}
                </div>

                <p>
                    <strong>Temperatura atual:</strong>
                    ${temperatura} °C
                </p>
            `;
        })

        // Caso aconteça algum erro
        .catch(erro => {

            resultado.innerHTML = `
                <p>
                    Não foi possível consultar os dados do clima.
                </p>
            `;

            console.error(erro);
        });
});