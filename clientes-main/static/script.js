// Captura o formulário e a lista de clientes
const formCadastro = document.getElementById('formCadastro');
const listaClientes = document.getElementById('listaClientes');

// Função para adicionar cliente à lista
function adicionarCliente(nome, email, telefone) {
    const li = document.createElement('li');
    li.textContent = `Nome: ${nome} | Email: ${email} | Telefone: ${telefone}`;
    listaClientes.appendChild(li);
}

// Função para lidar com o envio do formulário
formCadastro.addEventListener('submit', function (event) {
    event.preventDefault(); // Evita o envio padrão do formulário

    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const telefone = document.getElementById('telefone').value;

    // Chama a função para adicionar o cliente à lista
    adicionarCliente(nome, email, telefone);

    // Limpa os campos após o cadastro
    formCadastro.reset();
});