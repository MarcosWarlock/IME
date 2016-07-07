/*
 
O script deve ser executado na pagina http://www.ime.eb.br/provas-anteriores-cfg.html

*/

var links = document.querySelectorAll('a[href*="pdf"]');
var i;
for (i in links) 
{
	window.open(links[i].href);
}
