// Função de login
function logar() {
    var login = document.getElementById('userName').value;
    var senha = document.getElementById('userPassword').value;
    var tipoUser = document.getElementById('tipoUser').value;

}

// Função de cadastro de usuário
function cadastrar() {
    var novoUsuario = document.getElementById('newUser').value;
    var novaSenha = document.getElementById('newPassword').value;
    var tipoUser = document.getElementById('tipoUser').value;

    // Aqui envia os dados para o back-end para salvar
    if (novoUsuario && novaSenha) {
        alert(`Usuário ${novoUsuario} cadastrado com sucesso!`);
    } else {
        alert('Preencha os campos de cadastro corretamente.');
    }
}

// Toggle responsivo no menu de navegação
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

// Função para salvar produtos
function salvarProduto() {
    var nomeProduto = document.getElementById('nomeProduto').value;
    var precoProduto = document.getElementById('precoProduto').value;

    if (nomeProduto && precoProduto) {
        alert(`Produto ${nomeProduto} salvo com sucesso ao preço de R$ ${precoProduto}`);
    } else {
        alert('Preencha todos os campos de produto.');
    }

    function redirecionarParaLogin() {
    window.location.href = "/logar";
}
}
