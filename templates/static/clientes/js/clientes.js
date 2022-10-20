function add_ativo(){
    container = document.getElementById('form-ativo')

    html = "<br>  <div class='row'> <div class='col-md'> <input type='text' placeholder='Ativo' class='form-control' name='codigo_ativo' > </div> <div class='col-md'><input type='text' placeholder='Quantidade' class='form-control' name='quantidade_ativos' ></div> <div class='col-md'> <input type='number' step='0.01' placeholder='Preço' class='form-control' name='preco'> </div> <div class='col-md'><input type='text' placeholder='Operação' class='form-control' name='operacao' ></div> <div class='col-md'><input type='date' placeholder='Data da operação' class='form-control' name='data_operacao' ></div> </div>"

    container.innerHTML += html
}

function exibir_form(tipo){

    add_cliente = document.getElementById('add_cliente')
    att_cliente = document.getElementById('att_cliente')

    if(tipo == "1"){
        att_cliente.style.display = "none"
        add_cliente.style.display = "block"

    }else if(tipo == "2"){
        att_cliente.style.display = "block"
        add_cliente.style.display = "none"
    }
}


function dados_cliente(){
    cliente = document.getElementById('cliente-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_cliente = cliente.value

    data = new FormData()
    data.append('id_cliente', id_cliente)
    
    fetch("/clientes/atualiza_cliente/",{
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data

    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('form-att-cliente').style.display = 'block'

        id = document.getElementById('id')
        id.value = data['cliente_id']

        nome = document.getElementById('nome')
        nome.value = data['cliente']['nome']

        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['cliente']['sobrenome']

        cpf = document.getElementById('cpf')
        cpf.value = data['cliente']['cpf']

        email = document.getElementById('email')
        email.value = data['cliente']['email']

        div_ativos = document.getElementById('ativos')
        console.log(div_ativos)
        
        for(i=0; i<data['ativos'].length; i++){
            div_ativos.innerHTML += "\<form action='/clientes/update_ativo/" + data['ativos'][i]['id'] +"' method='POST'>\
                <div class='row'>\
                        <div class='col-md'>\
                            <input class='form-control' name='ativo' type='text' value='" + data['ativos'][i]['fields']['codigo_ativo'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control' name='quantidade' type='text' value='" + data['ativos'][i]['fields']['quantidade_ativos'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control' type='text' name='preco' value='" + data['ativos'][i]['fields']['preco'] + "' >\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control' type='text' name='data' value='" + data['ativos'][i]['fields']['data_operacao'] + "' >\
                        </div>\
                        <div class='col-md'>\
                            <input class='btn btn-lg btn-success' type='submit'>\
                        </div>\
                    </form>\
                    <div class='col-md'>\
                        <a href='/clientes/excluir_ativo/"+ data['ativos'][i]['id'] +"' class='btn btn-lg btn-danger'>EXCLUIR</a>\
                    </div>\
                </div><br>"
        }
        
    })


}


function update_cliente(){
    nome = document.getElementById('nome').value
    sobrenome = document.getElementById('sobrenome').value
    email = document.getElementById('email').value
    cpf = document.getElementById('cpf').value
    id = document.getElementById('id').value

    fetch('/clientes/update_cliente/' + id, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            nome: nome,
            sobrenome: sobrenome,
            email: email,
            cpf: cpf,
        })

    }).then(function(result){
        return result.json()
    }).then(function(data){

        if(data['status'] == '200'){
            nome = data['nome']
            sobrenome = data['sobrenome']
            email = data['email']
            cpf = data['cpf']
            console.log('Dados alterado com sucesso')
        }else{
            console.log('Ocorreu algum erro')
        }

    })

}