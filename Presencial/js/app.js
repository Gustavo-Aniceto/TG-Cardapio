
$(document).ready(function () { // pega o elemento "document", após ele está todo carregado
    cardapio.eventos.init();
});

var cardapio = {};

var MEU_CARRINHO = [];
var MEU_ENDERECO = null;

var VALOR_CARRINHO = 0;


CELULAR_EMPRESA = '5511958705804';

cardapio.eventos = {
    init: () => {
        cardapio.metodos.obterItensCardapio();

    }
}


cardapio.metodos = {

    // obtem a lista de itens do cardápio
    obterItensCardapio: (categoria = 'Tradicionais', vermais = false) => {
        var filtro = MENU[categoria];

        if (!vermais) {
            $("#itensCardapio").html('')
            $("#btnVerMais").removeClass('hidden');
        }

        $.each(filtro, (i, e) => {
            let temp = cardapio.templates.item.replace(/\${img}/g, e.img)
                .replace(/\${name}/g, e.name)
                .replace(/\${price}/g, e.price.toFixed(2).replace('.', ','))
                .replace(/\${id}/g, e.id);

            if (vermais && i >= 8 && i < 12) {
                $("#itensCardapio").append(temp)
            }

            if (!vermais && i < 8) {
                $("#itensCardapio").append(temp)
            }
        })

        // remove o ativo
        $(".container-menu a").removeClass('active');

        // seta o menu para ativo
        $("#menu-" + categoria).addClass('active');
    },

    // Clique no botão de ver mais
    verMais: () => {
        var ativo = $(".container-menu a.active").attr('id').split('menu-')[1];
        cardapio.metodos.obterItensCardapio(ativo, true);

        $("#btnVerMais").addClass('hidden');
    },

    // Diminuir a quantidade do item no cardápio
    diminuirQuantidade: (id) => {
        let qntdAtual = parseInt($('#qntd-' + id).text());

        if (qntdAtual > 0) {
            $('#qntd-' + id).text(qntdAtual - 1)
        }
    },

    // Aumentar a quantidade do item no cardápio
    aumentarQuantidade: (id) => {
        let qntdAtual = parseInt($('#qntd-' + id).text());

        $('#qntd-' + id).text(qntdAtual + 1)
    },

    // Adicionar ao carrinho o item do cardápio
    adicionarAoCarrinho: (id) => {
        let qntdAtual = parseInt($('#qntd-' + id).text());
    
        if (qntdAtual > 0) {
            // Obter a categoria ativa
            var categoria = $(".container-menu a.active").attr('id').split('menu-')[1];
            
            // Obter a lista de itens da categoria
            let filtro = MENU[categoria];
    
            // Encontrar o item correspondente ao id
            let item = $.grep(filtro, (e, i) => { return e.id == id });
    
            if (item.length > 0) {
                // Verificar se o item já existe no carrinho
                let existe = $.grep(MEU_CARRINHO, (elem, index) => { return elem.id == id });
    
                // Caso já exista o item no carrinho, apenas altera a quantidade
                if (existe.length > 0) {
                    let objIndex = MEU_CARRINHO.findIndex((obj => obj.id == id));
                    MEU_CARRINHO[objIndex].qntd += qntdAtual;
                } else {
                    // Caso não exista o item no carrinho, adiciona-o
                    item[0].qntd = qntdAtual;
                    MEU_CARRINHO.push(item[0]);
                }
            }
        }
    
        cardapio.metodos.mensagem('Item adicionado ao carrinho', 'green');
        $('#qntd-'+id).text(0);

        cardapio.metodos.atualizarBadgeTotal();
    },
    


    atualizarBadgeTotal: () => {
        var total = 0;

        $.each(MEU_CARRINHO, (i, e) => {
            total += e.qntd
        })

        if (total > 0) {
            $(".botao-carrinho").removeClass('hidden')
            $(".container-total-carrinho").removeClass('hidden')
        } else {
            $(".botao-carrinho").addClass('hidden')
            $(".container-total-carrinho").addClass('hidden')
        }

        $(".badge-total-carrinho").html(total);
    },

    // abrir a modal de carrinho
    abrirCarrinho: (abrir) => {
        const modalCarrinho = $('#modalCarrinho');
        if (abrir) {
            modalCarrinho.removeClass('hidden');
            cardapio.metodos.carregarCarrinho();
        } else {
            modalCarrinho.addClass('hidden');
        }
    },

    carregarEtapa: (etapa) => {
        const lblTituloEtapa = $("#lblTituloEtapa");
        const itensCarrinho = $("#itensCarrinho");
        const localEntrega = $("#localEntrega");
        const resumoCarrinho = $("#resumoCarrinho");
        const pagamento = $("#pagamento");
        const botaoVoltar = $("#btnVoltar");

        // Função auxiliar para esconder todos os conteúdos e botões
        const esconderTodos = () => {
            itensCarrinho.addClass('hidden');
            localEntrega.addClass('hidden');
            resumoCarrinho.addClass('hidden');
            pagamento.addClass('hidden');
            $(".etapa").removeClass('active');
            $("#btnEtapaPedido, #btnEtapaEndereco, #btnEtapaResumo, #btnEtapaPagamento").addClass('hidden');
        };

        esconderTodos(); // Esconde todos inicialmente

        if (etapa === 1) {
            lblTituloEtapa.text('Seu carrinho:');
            itensCarrinho.removeClass('hidden');
            $(".etapa1").addClass('active');
            $("#btnEtapaPedido").removeClass('hidden');
            botaoVoltar.addClass('hidden');
        }
        else if (etapa === 2) {
            lblTituloEtapa.text('Endereço de entrega:');
            localEntrega.removeClass('hidden');
            $(".etapa1, .etapa2").addClass('active');
            $("#btnEtapaEndereco").removeClass('hidden');
            botaoVoltar.removeClass('hidden');
        }
        else if (etapa === 3) {
            lblTituloEtapa.text('Resumo do pedido:');
            resumoCarrinho.removeClass('hidden');
            $(".etapa1, .etapa2, .etapa3").addClass('active');
            $("#btnEtapaResumo").removeClass('hidden');
            botaoVoltar.removeClass('hidden');
        }
        else if (etapa === 4) {
            lblTituloEtapa.text('Realizar pagamento:');
            pagamento.removeClass('hidden');
            $(".etapa1, .etapa2, .etapa3, .etapa4").addClass('active');
            $("#btnEtapaPagamento").removeClass('hidden');
            botaoVoltar.removeClass('hidden');
        }
    },

    // botão de voltar etapa
    voltarEtapa: () => {

        let etapa = $(".etapa.active").length;
        cardapio.metodos.carregarEtapa(etapa - 1);

    },

    // carrega a lista de itens do carrinho
    carregarCarrinho: () => {

        cardapio.metodos.carregarEtapa(1);

        if(MEU_CARRINHO.length > 0) {

            $("#itensCarrinho").html('');

            $.each(MEU_CARRINHO, (i, e) => {
                let temp = cardapio.templates.itemCarrinho.replace(/\${img}/g, e.img)
                .replace(/\${nome}/g, e.name)
                .replace(/\${preco}/g, e.price.toFixed(2).replace('.', ','))
                .replace(/\${id}/g, e.id)
                .replace(/\${dsc}/g, produto.dsc || "Descrição não disponível")
                .replace(/\${qntd}/g, e.qntd);

                $("#itensCarrinho").append(temp);

                // ultimo item
                if((i+1) == MEU_CARRINHO.length) {
                    cardapio.metodos.carregarValores();
                }
            })
        } else {
            $("#itensCarrinho").html('<p class="carrinho-vazio"><i class="fa fa-shopping-bag"></i> Seu carrinho esta vazio.</p');
            cardapio.metodos.carregarValores();
        }
    },

    // diminuir a quantidade do item no carrinho
    diminuirQuantidadeCarrinho: (id) => {
        let qntdAtual = parseInt($('#qntd-carrinho-'+id).text()); 

        if(qntdAtual > 1) {
            $('#qntd-carrinho-'+id).text(qntdAtual - 1);
            cardapio.metodos.atualizarCarrinho(id, qntdAtual - 1);
        } else {
            cardapio.metodos.removerItemCarrinho(id);
        }
    },

    // aumentar a quantidade do item no carrinho
    aumentarQuantidadeCarrinho: (id) => {
        let qntdAtual = parseInt($('#qntd-carrinho-'+id).text());
        $('#qntd-carrinho-'+id).text(qntdAtual + 1);
        cardapio.metodos.atualizarCarrinho(id, qntdAtual + 1);
    },

    // botão remover item do carrinho
    removerItemCarrinho: (id) => {
        MEU_CARRINHO = $.grep(MEU_CARRINHO, (e, i) => { return e.id != id });
        cardapio.metodos.carregarCarrinho();

        // atualiza o botão carrinho com a quantidade atualizada
        cardapio.metodos.atualizarBadgeTotal();
    },

    // atualiza o carrinho com a quantidade atual
    atualizarCarrinho: (id, qntd) => {

        let objIndex = MEU_CARRINHO.findIndex((obj => obj.id == id));
        MEU_CARRINHO[objIndex].qntd = qntd;

        // atualiza o botão carrinho com a quantidade atualizada
        cardapio.metodos.atualizarBadgeTotal();
        
        // atualiza os valores (R$) totais do carrinho
        cardapio.metodos.carregarValores();
    },

    // carrega os valores de SubTotal, Entrega e Total
    carregarValores: () => {
        VALOR_CARRINHO = 0;

        $("#lblSubTotal").text('R$ 0,00');;
        $("#lblValorTotal").text('R$ 0,00');

        $.each(MEU_CARRINHO, (i, e) => {
            VALOR_CARRINHO += parseFloat(e.price * e.qntd);

            if((i + 1) == MEU_CARRINHO.length) {
                $("#lblSubTotal").text(`R$ ${VALOR_CARRINHO.toFixed(2).replace('.', ',')}`);
                $("#lblValorTotal").text(`R$ ${(VALOR_ENTREGA + VALOR_CARRINHO).toFixed(2).replace('.', ',')}`);
            }
        })
    },

    carregarEndereco: () => {
        if(MEU_CARRINHO.length <= 0) {
            cardapio.metodos.mensagem('Seu carrinho está vazio.');
            return;
        }

        cardapio.metodos.carregarEtapa(2);
    },

    // API ViaCEP
    buscarCep: () => {

        // cria a variavel com o valor do cep
        var cep = $("#txtCEP").val().trim().replace(/\D/g, '');

        // verifica se o CEP possui valor informado
        if(cep != "") {
            // Expressão regular para validar o CEP
            var validacep = /^[0-9]{8}$/;

            if(validacep.test(cep)) {

                $.getJSON("https://viacep.com.br/ws/"+cep+"/json/?callback=?", function (dados) {
                    if(!("erro" in dados)) {
                        // atualizar os campos com valores retornados 
                        $("#txtEndereco").val(dados.logradouro);
                        $("#txtBairro").val(dados.bairro);
                        $("#txtCidade").val(dados.localidade);
                        $("#ddlUf").val(dados.uf);
                        $("#txtNumero").focus();
                    } else {
                        cardapio.metodos.mensagem('CEP não encontrado. Preencha as informações manualmente.');
                        $("#txtEndereco").focus(); 
                    }
                })

            } else {
                cardapio.metodos.mensagem('Formato de CEP inválido.');
                $("#txtCEP").focus(); 
            }
        } else {
            cardapio.metodos.mensagem('Informe o CEP, por favor.');
            $("#txtCEP").focus();
        }
    },

    // validação antes de prosseguir para a etapa 3
    resumoPedido: () => {

        let cep = $("#txtCEP").val().trim();
        let endereco = $("#txtEndereco").val().trim();
        let bairro = $("#txtBairro").val().trim();
        let cidade = $("#txtCidade").val().trim();
        let uf = $("#ddlUf").val().trim();
        let numero = $("#txtNumero").val().trim();
        let complemento = $("#txtComplemento").val().trim();

        if(cep.length <= 0) {
            cardapio.metodos.mensagem('Informe o CEP, por favor.');
            $("#txtCEP").focus();
            return;
        }

        if(endereco.length <= 0) {
            cardapio.metodos.mensagem('Informe o Endereço, por favor.');
            $("#txtEndereco").focus();
            return;
        }

        if(bairro.length <= 0) {
            cardapio.metodos.mensagem('Informe o Bairro, por favor.');
            $("#txtBairro").focus();
            return;
        }

        if(cidade.length <= 0) {
            cardapio.metodos.mensagem('Informe o Cidade, por favor.');
            $("#txtCidade").focus();
            return;
        }

        if(uf == "-1") {
            cardapio.metodos.mensagem('Informe o UF, por favor.');
            $("#ddlUf").focus();
            return;
        }

        if(numero.length <= 0) {
            cardapio.metodos.mensagem('Informe o Número, por favor.');
            $("#txtNumero").focus();
            return;
        }

        MEU_ENDERECO = {
            cep: cep,
            endereco: endereco,
            bairro: bairro,
            cidade: cidade,
            uf: uf,
            numero: numero,
            complemento: complemento
        }

        cardapio.metodos.carregarEtapa(3);
        cardapio.metodos.carregarResumo();
    },

    // carrega a etapa de Resumo do pedido
    carregarResumo: () => {

        $("#listaItensResumo").html('');

        $.each(MEU_CARRINHO, (i, e) => {
            let temp = cardapio.templates.itemResumo.replace(/\${img}/g, e.img)
                .replace(/\${nome}/g, e.name)
                .replace(/\${preco}/g, e.price.toFixed(2).replace('.', ','))
                .replace(/\${qntd}/g, e.qntd);

            $("#listaItensResumo").append(temp);
        })

        $("#resumoEndereco").html(`${MEU_ENDERECO.endereco}, ${MEU_ENDERECO.numero}, ${MEU_ENDERECO.bairro}`)
        $("#cidadendereco").html(`${MEU_ENDERECO.cidade}-${MEU_ENDERECO.uf} / ${MEU_ENDERECO.cep} ${MEU_ENDERECO.complemento}`)
    
        cardapio.metodos.finalizarPedido();
    },

    // Atualiza o link do botão do WhatsApp
    finalizarPedido: () => {

        if(MEU_CARRINHO.length > 0 && MEU_ENDERECO != null) {
            var texto = 'Olá! gostaria de fazer um pedido:';
            texto += `\n*Itens do pedido:*\n\n\${itens}`;
            texto += '\n*Endereço de entrega:*';
            texto += `\n${MEU_ENDERECO.endereco}, ${MEU_ENDERECO.numero}, ${MEU_ENDERECO.bairro}`;
            texto += `\n${MEU_ENDERECO.cidade}-${MEU_ENDERECO.uf} / ${MEU_ENDERECO.cep} ${MEU_ENDERECO.complemento}`;
            texto += `\n\n*Total: R$ ${(VALOR_CARRINHO + VALOR_ENTREGA).toFixed(2).replace('.', ',')}*`;

            var itens = '';

            $.each(MEU_CARRINHO, (i, e) => {
                itens += `*${e.qntd}x* ${e.name} ........ R$ ${e.price.toFixed(2).replace('.', ',')} \n`;
            
                if((i+1) == MEU_CARRINHO.length) {

                    texto = texto.replace(/\${itens}/g, itens);

                    // converte a URL
                    let encode = encodeURI(texto);
                    let URL = `https://wa.me/${CELULAR_EMPRESA}?text=${encode}`;

                    $("#btnEtapaResumo").attr('href', URL);
                }
            })
        }

    },
}

cardapio.templates = {
    item: `
        <div class="col-12 col-lg-3 col-md-3 col-sm-6 mb-5 animated fadeInUp">
            <div class="card card-item" id="\${id}">
                <div class="img-produto">
                    <img src="\${img}" />
                </div>
                <p class="title-produto text-center mt-4">
                    <b>\${name}</b>
                </p>
                <p class="price-produto text-center">
                    <b>R$ \${price}</b>
                </p>
                <div class="add-carrinho">
                <p class="card-text">\${dsc}</p>
                    <span class="btn-menos" onclick="cardapio.metodos.diminuirQuantidade('\${id}')"><i class="fas fa-minus"></i></span>
                    <span class="add-numero-itens" id="qntd-\${id}">0</span>
                    <span class="btn-mais" onclick="cardapio.metodos.aumentarQuantidade('\${id}')"><i class="fas fa-plus"></i></span>
                    <span class="btn btn-add" onclick="cardapio.metodos.adicionarAoCarrinho('\${id}')"><i class="fa fa-shopping-bag"></i></span>
                </div>
            </div>
        </div>
    `,

    itemCarrinho: `
        <div class="col-12 item-carrinho">
            <div class="img-produto">
                <img src="\${img}" />
            </div>
            <div class="dados-produto">
                <p class="title-produto"><b>\${nome}</b></p>
                <p class="price-produto"><b>R$ \${preco}</b></p>
            </div>
            <div class="add-carrinho">
                <span class="btn-menos" onclick="cardapio.metodos.diminuirQuantidadeCarrinho('\${id}')"><i class="fas fa-minus"></i></span>
                <span class="add-numero-itens" id="qntd-carrinho-\${id}">\${qntd}</span>
                <span class="btn-mais" onclick="cardapio.metodos.aumentarQuantidadeCarrinho('\${id}')"><i class="fas fa-plus"></i></span>
                <span class="btn btn-remove no-mobile" onclick="cardapio.metodos.removerItemCarrinho('\${id}')"><i class="fa fa-times"></i></span>
            </div>
        </div>
    `,

    itemResumo: `
        <div class="col-12 item-carrinho resumo">
            <div class="img-produto-resumo">
                <img src="\${img}" />
            </div>
            <div class="dados-produto">
                <p class="title-produto-resumo">
                    <b>\${nome}</b>
                </p>
                <p class="price-produto-resumo">
                    <b>R$ \${preco}</b>
                </p>
            </div>
            <p class="quantidade-produto-resumo">
                x <b>\${qntd}</b>
            </p>
        </div>
    `
}



function carregarBotaoLigar() {
    const nome = $('#nome').val();
    const data = $('#data').val();
    const hora = $('#hora').val();
    const pessoas = $('#pessoas').val();

    // Verificar se todos os campos foram preenchidos
    if (!nome || !data || !hora || !pessoas) {
        mensagem("Por favor, preencha todos os campos!", "red");
        return;
    }

    let texto = `Olá! Gostaria de fazer uma *reserva*.\nNome: ${nome}\nData: ${data}\nHora: ${hora}\nNúmero de Pessoas: ${pessoas}`;
    let encode = encodeURIComponent(texto);
    let URL = `https://wa.me/${CELULAR_EMPRESA}?text=${encode}`;

    window.open(URL, '_blank');
}

function validarReserva() {
    const data = new Date(document.getElementById('data').value);
    const hoje = new Date();

    // Verifica se a data é válida e não é anterior ao dia de hoje
    if (data < hoje) {
        alert('Por favor, escolha uma data futura.');
        return false; // Impede o envio do formulário
    }
    return true; // Permite o envio do formulário
}

