const myfile=document.querySelector('input[type=file]')
const label = document.querySelector('.label');
myfile.addEventListener('change',function(e){
    a=myfile.files[0];
    label.innerHTML=a.name;
    const reader= new FileReader()
    // reader.onload=function(){
    //     console.log(reader.result);
    // }
    reader.readAsText(a)
},false)