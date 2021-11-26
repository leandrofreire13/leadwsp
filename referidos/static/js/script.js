//Pega texto
var str = document.getElementById("textostatus").textContent;
console.log('To aqui');
//conta o texto
var count = (str.match(/Iniciar/g) || []).length;
document.getElementById("res").textContent = count


/*
<!--
  Iniciar - ok
  Ligação 1
  Ligação 2
  Ligação 3
  Mandar áudio
  Áudio enviado
  Agendado
  Mandar texto
  Texto enviado
  Não venda
  Venda
-->
*/