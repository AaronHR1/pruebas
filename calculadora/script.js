let numero=0;
let numeroAnt=0;
let operacion="";

function insertarNumero(x){
    numero= (numero*10)+x
   
    document.getElementById('cantidad').textContent=numero;
}

function suma(){
    numeroAnt = numero;
    numero=0;
    operacion="suma"
    document.getElementById('cantidad').textContent=numero;
}
function resta(){
    numeroAnt = numero;
    numero=0;
    operacion="resta"
    document.getElementById('cantidad').textContent=numero;
    
}
function multiplicacion(){
    numeroAnt = numero;
    numero=0;
    operacion="multiplicacion"
    document.getElementById('cantidad').textContent=numero;
    
}
function divicion(){
    numeroAnt = numero;
    numero=0;
    operacion="divicion"
    document.getElementById('cantidad').textContent=numero;
    
}
function igual(){
    if (operacion=="suma"){
        numero=numeroAnt+numero
    }
    else if (operacion=="resta"){
        numero=numeroAnt-numero
    }
    else if (operacion=="multiplicacion"){
        numero=numeroAnt*numero
    }
    else if (operacion=="divicion"){
        numero=numeroAnt/numero
    }
    document.getElementById('cantidad').textContent=numero;
}


function delet(){
    numero=numero/10;
    numero=Math.floor(numero);
    document.getElementById('cantidad').textContent=numero;
}
function clean(){
    numero=0;
    document.getElementById('cantidad').textContent=numero;
}