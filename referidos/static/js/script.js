//Pega texto
var str = document.getElementById("textostatus").textContent;
console.log('To aqui');
//conta o texto

if(str.match(/Iniciar/g)){
    var count = (str.match(/Iniciar/g) || []).length;
    document.getElementById("ini").textContent = count
}
if(str.match(/Ligação 1/g)){
    var count = (str.match(/Ligação 1/g) || []).length;
    document.getElementById("lig1").textContent = count
}
if(str.match(/Ligação 2/g)){
    var count = (str.match(/Ligação 2/g) || []).length;
    document.getElementById("lig2").textContent = count
}

if(str.match(/Ligação 3/g)){
    var count = (str.match(/Ligação 3/g) || []).length;
    document.getElementById("lig3").textContent = count
}

if(str.match(/Mandar áudio/g)){
    var count = (str.match(/Mandar áudio/g) || []).length;
    document.getElementById("maud").textContent = count
}

if(str.match(/Áudio enviado/g)){
    var count = (str.match(/Áudio enviado/g) || []).length;
    document.getElementById("aud").textContent = count
}

if(str.match(/Agendado/g)){
    var count = (str.match(/Agendado/g) || []).length;
    document.getElementById("agen").textContent = count
}

if(str.match(/Mandar texto/g)){
    var count = (str.match(/Mandar texto/g) || []).length;
    document.getElementById("mtext").textContent = count
}

if(str.match(/Texto enviado/g)){
    var count = (str.match(/Texto enviado/g) || []).length;
    document.getElementById("text").textContent = count
}

if(str.match(/Não venda/g)){
    var count = (str.match(/Não venda/g) || []).length;
    document.getElementById("nven").textContent = count
}

if(str.match(/Venda/g)){
    var count = (str.match(/Venda/g) || []).length;
    document.getElementById("ven").textContent = count
}

