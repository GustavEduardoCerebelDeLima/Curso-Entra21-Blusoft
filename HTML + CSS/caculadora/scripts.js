function insert(num){
    let number = document.getElementById('result').innerHTML;
    document.getElementById('result').innerHTML = number + num;
}

function clean(){
    document.getElementById('result').innerHTML = '';
}

function del(){
    let result = document.getElementById('result').innerHTML;
    document.getElementById('result').innerHTML = result.substring(0, result.length - 1);
}

function calc(){
    let calc = document.getElementById('result').innerHTML;
    if(calc){
        document.getElementById('result').innerHTML = eval(calc);
    }
}