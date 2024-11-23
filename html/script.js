document.getElementById('consulta-formulario').addEventListener('submit', function(event) {
    event.preventDefault();

    const id = document.getElementById('id_persona').value;

    fetch(`/cgi-bin/consultas.py?id=${id}`)
        .then(response => response.text())
        .then(data => {
            document.getElementById('resultado').innerHTML = data;
        })
        .catch(error => console.error('Error:', error));
});