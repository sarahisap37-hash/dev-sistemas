const caixas = document.querySelectorAll(".caixa");

caixas.forEach(function(caixa) {

    caixa.addEventListener("dblclick", function() {

        console.log(this);

        if (this.id === "caixa1") {
            alert("Vermelho");
            this.style.backgroundColor = "pink";
        }

        if (this.id === "caixa2") {
            alert("Verde");
            this.style.backgroundColor = "lightgreen";
        }

        if (this.id === "caixa3") {
            alert("Azul");
            this.style.backgroundColor = "lightblue";
        }

    });

});