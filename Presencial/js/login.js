document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const usuario = document.getElementById('usuario').value;
    const senha = document.getElementById('senha').value;

    // Simulação de verificação de login
    if (usuario === "admin" && senha === "0210") {
        window.location.href = "administrativo.html"; // Redirecionar
    } else {
        alert("Usuário ou senha incorretos.");
    }
});
