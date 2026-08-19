const botao = document.getElementById("buscar");
const resultado = document.getElementById("resultado");

botao.addEventListener("click", function () {

    const cep = document.getElementById("cep").value;

    if (cep.length !== 8 || isNaN(cep)) {
        resultado.innerHTML = "<p>CEP inválido ou não localizado.</p>";
        return;
    }

    const url = `https://viacep.com.br/ws/${cep}/json/`;

    fetch(url)
        .then(response => response.json())
        .then(dados => {

            if (dados.erro) {
                resultado.innerHTML = "<p>CEP inválido ou não localizado.</p>";
                return;
            }

            resultado.innerHTML = `
                <h2>Endereço encontrado</h2>
                <p><strong>Logradouro:</strong> ${dados.logradouro}</p>
                <p><strong>Bairro:</strong> ${dados.bairro}</p>
                <p><strong>Cidade:</strong> ${dados.localidade}</p>
                <p><strong>UF:</strong> ${dados.uf}</p>
            `;
        })
        .catch(erro => {
            resultado.innerHTML =
                "<p>Não foi possível realizar a consulta.</p>";

            console.error(erro);
        });
});