$(document).ready(function(){
$('select').material_select(); 



var previewImage = function(event) {
    var preview = document.getElementById('preview');
    preview.src = URL.createObjectURL(event.target.files[0]);
      };
      
function test(){
    console.log(test);
    };

});