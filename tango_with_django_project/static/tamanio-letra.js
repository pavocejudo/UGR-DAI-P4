
$(document).ready(function(){
    $('.btn-default').click(function(){ /*al hacer click en un elemento con la clase btn*/
       /*borre todas las clases*/
        if($(this).attr('id') == 'grande'){  /*si la clase botón tiene el ID grande*/
            $('body').css('font-size','18px');  /* cambio el tamaño a 18px */
        }
        else if(this.id == 'peque'){ /*si el ID es disminuir*/
            $('body').css('font-size','9px'); /*cargue la clase chica*/
        }
        else if(this.id == "normal"){
            $('body').css('font-size','');
        }
        /*agregue la negrita al botón activo*/
    });
});

/*EFECTO HOVER*/

$(document).ready(function() {
    $('.btn').hover(function() {
        $(this).css('background-color','#BDBDBD'); /*agregue efecto hover*/
    }, function() {
        $(this).css('background-color','');  /*quite efecto hover*/
    });
});
