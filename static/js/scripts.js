// Função de login
function logar() {
    var login = document.getElementById('userName').value;
    var senha = document.getElementById('userPassword').value;
    var tipoUser = document.getElementById('tipoUser').value;

    // Aqui você pode usar fetch para enviar os dados para o backend
    fetch('/logar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({usuario: login, password: senha, tipoUser: tipoUser})
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Redirecionar ou atualizar a interface do usuário
                window.location.href = '/';
            } else {
                alert('Erro: ' + data.message);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

// Função de cadastro de usuário
function cadastrar() {
    var novoUsuario = document.getElementById('newUser').value;
    var novaSenha = document.getElementById('newPassword').value;
    var tipoUser = document.getElementById('tipoUser').value;

    if (novoUsuario && novaSenha) {
        fetch('/cadastrar/usuario', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({usuario: novoUsuario, password: novaSenha, tipoUser: tipoUser})
        })
            .then(response => response.json())
            .then(data => {
                alert(`Usuário ${novoUsuario} cadastrado com sucesso!`);
                // Redirecionar ou atualizar a interface do usuário
            })
            .catch((error) => {
                console.error('Error:', error);
            });
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
        fetch('/produtos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({nome: nomeProduto, preco: precoProduto})
        })
            .then(response => response.json())
            .then(data => {
                alert(`Produto ${nomeProduto} salvo com sucesso ao preço de R$ ${precoProduto}`);
                // Redirecionar ou atualizar a interface do usuário
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    } else {
        alert('Preencha todos os campos de produto.');
    }
}

// Função para redirecionar para a página de login
function redirecionarParaLogin() {
    window.location.href = "/logar";
}
